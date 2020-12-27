"""Add background jobs

Revision ID: 95fd62c2fd4f
Revises: 8b6297128973
Create Date: 2020-12-27 14:53:11.896824

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "95fd62c2fd4f"
down_revision = "8b6297128973"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "background_jobs",
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("job_type", sa.Enum("send_email", name="backgroundjobtype"), nullable=False),
        sa.Column(
            "state",
            sa.Enum("pending", "working", "completed", "error", "failed", name="backgroundjobstatus"),
            nullable=False,
        ),
        sa.Column("queued", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("next_attempt", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("try_count", sa.Integer(), nullable=False),
        sa.Column("max_tries", sa.Integer(), nullable=False),
        sa.Column("payload", sa.LargeBinary(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_background_jobs")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("background_jobs")
    # ### end Alembic commands ###
