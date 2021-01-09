"""
Models for background jobs and scheduled jobs
"""
import enum

from sqlalchemy import BigInteger, Column, DateTime, Enum, Integer
from sqlalchemy import LargeBinary as Binary
from sqlalchemy import String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func

from couchers.models.base import Base


class BackgroundJobType(enum.Enum):
    # payload: org.couchers.internal.jobs.SendEmailPayload
    send_email = 1
    # payload: google.protobuf.Empty
    purge_login_tokens = 2


class BackgroundJobState(enum.Enum):
    # job is fresh, waiting to be picked off the queue
    pending = 1
    # job has been grabbed by a worker, and is being worked on
    working = 2
    # job complete
    completed = 3
    # error occured, will be retried
    error = 4
    # failed too many times, not retrying anymore
    failed = 5


class BackgroundJob(Base):
    """
    This table implements a queue of background jobs.
    """

    __tablename__ = "background_jobs"

    id = Column(BigInteger, primary_key=True)

    # used to discern which function should be triggered to service it
    job_type = Column(Enum(BackgroundJobType), nullable=False)
    state = Column(Enum(BackgroundJobState), nullable=False, default=BackgroundJobState.pending)

    # time queued
    queued = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # time at which we may next attempt it, for implementing exponential backoff
    next_attempt_after = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # used to count number of retries for failed jobs
    try_count = Column(Integer, nullable=False, default=0)

    max_tries = Column(Integer, nullable=False, default=2)

    # protobuf encoded job payload
    payload = Column(Binary, nullable=False)

    # if the job failed, we write that info here
    failure_info = Column(String, nullable=True)

    @hybrid_property
    def is_ready(self):
        return (
            (self.state == BackgroundJobState.pending)
            & (self.next_attempt_after <= func.now())
            & (self.try_count < self.max_tries)
        )


class RepeatedJobs(Base):
    """
    A job that's kicked off every n minutes
    """

    __tablename__ = "repeated_jobs"

    id = Column(BigInteger, primary_key=True)

    job_type = Column(Enum(BackgroundJobType), nullable=False)

    # number of minutes between kicking off these jobs
    run_every = Column(Integer, nullable=False)
