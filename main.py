import asyncio
if True:
  import os
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')
  cls()
  from keep_alive import keep_alive
  keep_alive()
  async def runn():
    while True:
      print("",end='')
      await asyncio.sleep(5)
  asyncio.run(runn())