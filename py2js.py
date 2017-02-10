# -*- coding: utf-8 -*-  

import PyV8

with PyV8.JSContext() as env1:
    env1.eval("""
function Encrypt(theText,text2) { 
  output = new String; 
  TextSize = theText.length; 
  while(text2.length<TextSize)
    text2+=text2
    
  Temp = new Array(); 
  for (I = 0; I < TextSize; I++) { 
    rnd = text2.charCodeAt(I); 
    Temp[I] = theText.charCodeAt(I) + rnd; 
  } 
  for (I = 0; I < TextSize; I++) { 
    output += Temp[I]+","; 
  }
  return output; 
} 

function test(str,str1) {
	return Encrypt(str,str1);
}
    """)
    vars = env1.locals
    var_i = vars.test('admin','aisino.kps.console')
    print var_i