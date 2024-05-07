import fire

def hello(name="World"):
  return "ABC Hello %s!!!" % name

if __name__ == '__main__':
  fire.Fire(hello)