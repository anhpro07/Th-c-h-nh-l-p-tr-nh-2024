print("LE TUAN ANH")
print("MSSV: 235752021610050")
class Nguoi(object):
 def getGender( self ):
  return "Unknown"

class Nam( Nguoi ):
 def getGender( self ):
  return "Nam"
class Nu( Nguoi ):
 def getGender( self ):
  return "Nu"
aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
