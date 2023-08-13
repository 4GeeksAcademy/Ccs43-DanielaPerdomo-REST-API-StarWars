"""empty message

Revision ID: d9dbe4a2c28c
Revises: 9e770ba4da35
Create Date: 2023-08-13 19:44:58.666353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9dbe4a2c28c'
down_revision = '9e770ba4da35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('birth_year', sa.String(length=50), nullable=False),
    sa.Column('species', sa.String(length=50), nullable=False),
    sa.Column('height', sa.String(length=50), nullable=False),
    sa.Column('mass', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('hair_color', sa.String(length=50), nullable=False),
    sa.Column('skin_color', sa.String(length=50), nullable=False),
    sa.Column('homeworld', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('birth_year'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('gender'),
    sa.UniqueConstraint('hair_color'),
    sa.UniqueConstraint('height'),
    sa.UniqueConstraint('homeworld'),
    sa.UniqueConstraint('mass'),
    sa.UniqueConstraint('skin_color'),
    sa.UniqueConstraint('species')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('populations', sa.String(length=50), nullable=False),
    sa.Column('rotarion_period', sa.String(length=50), nullable=False),
    sa.Column('orbital_period', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.String(length=50), nullable=False),
    sa.Column('gravity', sa.String(length=50), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('surface_water', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('diameter'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('gravity'),
    sa.UniqueConstraint('orbital_period'),
    sa.UniqueConstraint('populations'),
    sa.UniqueConstraint('rotarion_period'),
    sa.UniqueConstraint('surface_water'),
    sa.UniqueConstraint('terrain')
    )
    op.create_table('favCharacters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('characters_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['characters_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favPlanets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planets_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('name')

    op.drop_table('favPlanets')
    op.drop_table('favCharacters')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
