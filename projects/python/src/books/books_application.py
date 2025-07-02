import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')

from books.application_context_local import books_service

if __name__=='__main__':
    print(books_service.find_all())

