def data_type(s):

  if isinstance(s,str):
    return len(s)
  elif isinstance(s,type(none)):
      return"no value"
  elif isinstance(s,bool):
            return (s)
  elif isinstance(s, int):
            if s<100:
              return "less than 100"
            elif s>100:
              return"more than 100"
            else:
              return"equal to 100"

  elif isinstance(s,list):
    if len(s)>=[3]:
        return s [2]
    else:
        return s[2]