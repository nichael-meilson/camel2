"""create_main_tables

Revision ID: 8f43215c83c7
Revises: 
Create Date: 2022-06-18 18:20:15.514118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '8f43215c83c7'
down_revision = None
branch_labels = None
depends_on = None


def create_articles_table() -> None:
    op.create_table(
        "articles",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("author", sa.Text, nullable=False, index=True),
        sa.Column("title", sa.Text, nullable=False),
        sa.Column("date", sa.Text, nullable=False),
    )


def upgrade() -> None:
    create_articles_table()


def downgrade() -> None:
    op.drop_table("cleanings")
