"""Tweak nodes and clusters tables

Revision ID: 5140ed0b3be1
Revises: cce0606c2f41
Create Date: 2021-01-03 20:20:07.312542

"""
import geoalchemy2
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "5140ed0b3be1"
down_revision = "cce0606c2f41"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("clusters", sa.Column("official_cluster_for_node_id", sa.BigInteger(), nullable=False))
    op.create_index(
        op.f("ix_clusters_official_cluster_for_node_id"), "clusters", ["official_cluster_for_node_id"], unique=True
    )
    op.drop_index("ix_clusters_main_page_id", table_name="clusters")
    op.drop_constraint("fk_clusters_main_page_id_pages", "clusters", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_clusters_official_cluster_for_node_id_nodes"),
        "clusters",
        "nodes",
        ["official_cluster_for_node_id"],
        ["id"],
    )
    op.drop_column("clusters", "main_page_id")
    op.drop_index("ix_nodes_official_cluster_id", table_name="nodes")
    op.drop_constraint("fk_nodes_official_cluster_id_clusters", "nodes", type_="foreignkey")
    op.drop_column("nodes", "name")
    op.drop_column("nodes", "description")
    op.drop_column("nodes", "official_cluster_id")
    op.add_column("pages", sa.Column("main_page_for_cluster_id", sa.BigInteger(), nullable=True))
    op.create_index(op.f("ix_pages_main_page_for_cluster_id"), "pages", ["main_page_for_cluster_id"], unique=True)
    op.drop_index("ix_pages_owner_cluster_id", table_name="pages")
    op.create_index(op.f("ix_pages_owner_cluster_id"), "pages", ["owner_cluster_id"], unique=False)
    op.create_foreign_key(
        op.f("fk_pages_main_page_for_cluster_id_clusters"), "pages", "clusters", ["main_page_for_cluster_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("fk_pages_main_page_for_cluster_id_clusters"), "pages", type_="foreignkey")
    op.drop_index(op.f("ix_pages_owner_cluster_id"), table_name="pages")
    op.create_index("ix_pages_owner_cluster_id", "pages", ["owner_cluster_id"], unique=True)
    op.drop_index(op.f("ix_pages_main_page_for_cluster_id"), table_name="pages")
    op.drop_column("pages", "main_page_for_cluster_id")
    op.add_column("nodes", sa.Column("official_cluster_id", sa.BIGINT(), autoincrement=False, nullable=False))
    op.add_column(
        "nodes",
        sa.Column(
            "description",
            sa.VARCHAR(),
            server_default=sa.text("''::character varying"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column("nodes", sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key("fk_nodes_official_cluster_id_clusters", "nodes", "clusters", ["official_cluster_id"], ["id"])
    op.create_index("ix_nodes_official_cluster_id", "nodes", ["official_cluster_id"], unique=True)
    op.add_column("clusters", sa.Column("main_page_id", sa.BIGINT(), autoincrement=False, nullable=False))
    op.drop_constraint(op.f("fk_clusters_official_cluster_for_node_id_nodes"), "clusters", type_="foreignkey")
    op.create_foreign_key("fk_clusters_main_page_id_pages", "clusters", "pages", ["main_page_id"], ["id"])
    op.create_index("ix_clusters_main_page_id", "clusters", ["main_page_id"], unique=True)
    op.drop_index(op.f("ix_clusters_official_cluster_for_node_id"), table_name="clusters")
    op.drop_column("clusters", "official_cluster_for_node_id")
    # ### end Alembic commands ###
