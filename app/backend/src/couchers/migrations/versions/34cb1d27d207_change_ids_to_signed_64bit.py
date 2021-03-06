"""Change ids to signed 64bit

Revision ID: 34cb1d27d207
Revises: f85e551b9334
Create Date: 2020-12-17 14:08:19.721346

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "34cb1d27d207"
down_revision = "f85e551b9334"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "complaints", "author_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("complaints", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True)
    op.alter_column(
        "complaints", "reported_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column(
        "conversations",
        "id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        autoincrement=True,
        existing_server_default=sa.text("nextval('conversations_id_seq'::regclass)"),
    )
    op.alter_column(
        "friend_relationships",
        "from_user_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column("friend_relationships", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True)
    op.alter_column(
        "friend_relationships", "to_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column(
        "group_chat_subscriptions",
        "group_chat_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "group_chat_subscriptions", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True
    )
    op.alter_column(
        "group_chat_subscriptions",
        "last_seen_message_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "group_chat_subscriptions",
        "user_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "group_chats", "creator_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("group_chats", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger())
    op.alter_column(
        "host_requests",
        "from_last_seen_message_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "host_requests", "from_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("host_requests", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger())
    op.alter_column(
        "host_requests",
        "to_last_seen_message_id",
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "host_requests", "to_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column(
        "initiated_uploads", "user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column(
        "login_tokens", "user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("messages", "author_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False)
    op.alter_column(
        "messages", "conversation_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("messages", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True)
    op.alter_column("messages", "target_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=True)
    op.alter_column(
        "password_reset_tokens", "user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column(
        "references", "from_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("references", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True)
    op.alter_column(
        "references", "to_user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False
    )
    op.alter_column("sessions", "user_id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), existing_nullable=False)
    op.alter_column("users", "id", existing_type=sa.INTEGER(), type_=sa.BigInteger(), autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True)
    op.alter_column("sessions", "user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False)
    op.alter_column(
        "references", "to_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column("references", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True)
    op.alter_column(
        "references", "from_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "password_reset_tokens", "user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column("messages", "target_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=True)
    op.alter_column("messages", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True)
    op.alter_column(
        "messages", "conversation_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column("messages", "author_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False)
    op.alter_column(
        "login_tokens", "user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "initiated_uploads", "user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "host_requests", "to_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "host_requests",
        "to_last_seen_message_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column("host_requests", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER())
    op.alter_column(
        "host_requests", "from_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "host_requests",
        "from_last_seen_message_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column("group_chats", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER())
    op.alter_column(
        "group_chats", "creator_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column(
        "group_chat_subscriptions",
        "user_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "group_chat_subscriptions",
        "last_seen_message_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "group_chat_subscriptions", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True
    )
    op.alter_column(
        "group_chat_subscriptions",
        "group_chat_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "friend_relationships", "to_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column("friend_relationships", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True)
    op.alter_column(
        "friend_relationships",
        "from_user_id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "conversations",
        "id",
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        autoincrement=True,
        existing_server_default=sa.text("nextval('conversations_id_seq'::regclass)"),
    )
    op.alter_column(
        "complaints", "reported_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    op.alter_column("complaints", "id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), autoincrement=True)
    op.alter_column(
        "complaints", "author_user_id", existing_type=sa.BigInteger(), type_=sa.INTEGER(), existing_nullable=False
    )
    # ### end Alembic commands ###
