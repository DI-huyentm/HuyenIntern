# from fastapi import Body, FastAPI

# app = FastAPI()

# message = 'Tớ đi ra chỗ khác đây. Ngồi cạnh ngừi đẹp thiệt khó tập trung'

# @app.get("/message")
# async def read_all_message():
#     return message

# try:
#     x = int(input("Please enter a number: "))
#     print("done")
# except ValueError:
#     print("Oops!  That was no valid number.  Try again...")

import sys

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

  