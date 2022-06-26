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
        sa.Column("name", sa.Text, nullable=True, index=True),
        sa.Column("species", sa.Text, nullable=True),
        sa.Column("goal", sa.Text, nullable=True),
        sa.Column("num_lines", sa.Integer, nullable=True),
        sa.Column("setup", sa.Text, nullable=True),
        sa.Column("recipient", sa.Text, nullable=True),
        sa.Column("medium", sa.Text, nullable=True),
        sa.Column("selective_condition", sa.Text, nullable=True),
        sa.Column("cripple_mutant", sa.Boolean, nullable=True),
        sa.Column("how_cripple_mutant", sa.Text, nullable=True),
        sa.Column("env_type", sa.Text, nullable=True),
        sa.Column("how_type_env", sa.Text, nullable=True),
        sa.Column("changing_env", sa.Boolean, nullable=True),
        sa.Column("how_changing_env", sa.Text, nullable=True),
        sa.Column("env_type", sa.Text, nullable=True),
        sa.Column("how_type_env", sa.Text, nullable=True),
        sa.Column("complex_stressors", sa.Boolean, nullable=True),
        sa.Column("how_complex_stressors", sa.Text, nullable=True),
        sa.Column("num_generations", sa.Integer, nullable=True),
        sa.Column("abs_time", sa.Integer, nullable=True),
        sa.Column("contamination", sa.Text, nullable=True),
        sa.Column("fitness", sa.Boolean, nullable=True),
        sa.Column("fitness_param", sa.Text, nullable=True),
        sa.Column("competition", sa.Text, nullable=True),
        sa.Column("mutation_tracking", sa.Text, nullable=True),
        sa.Column("wgs", sa.Boolean, nullable=True),
        sa.Column("wgs_tech", sa.Text, nullable=True),
        sa.Column("wgs_platform", sa.Text, nullable=True),
        sa.Column("num_clones", sa.Integer, nullable=True),
        sa.Column("num_populations", sa.Integer, nullable=True),
        sa.Column("cov_clones", sa.Float, nullable=True),
        sa.Column("cov_populations", sa.Float, nullable=True),
        sa.Column("detection_lim", sa.Float, nullable=True),
        sa.Column("ngs_data_link", sa.Text, nullable=True),
        sa.Column("max_pop_size", sa.Integer, nullable=True),
        sa.Column("min_pop_size", sa.Integer, nullable=True),
        sa.Column("major_outcome", sa.Text, nullable=True),
        sa.Column("remarks", sa.Text, nullable=True),
        sa.Column("complete_mutation_data", sa.Boolean, nullable=True),
        sa.Column("reference_id", sa.Text, nullable=True),
        sa.Column("pmid", sa.Text, nullable=True),
        sa.Column("paper_url", sa.Text, nullable=True),
    )


def upgrade() -> None:
    create_articles_table()


def downgrade() -> None:
    op.drop_table("articles")
