# This file is for alembic

# Import all the models, so that Base has them before being
# imported by Alembic

from .database import Base
from api.v1.posts.models import Post
from api.v1.user.models import User
from api.v1.vote.models import Voter



