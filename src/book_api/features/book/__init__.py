# Export the books router to make it available to other modules
from .router import router as books_router

# Define what gets exported when someone imports from this package
__all__ = ["books_router"]