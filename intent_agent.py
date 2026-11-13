def detect(msg):
 m=msg.lower()
 if "saldo" in m:return {"intent":"saldo"}
 if "transfer" in m:return {"intent":"transferencia"}
 if "deposit" in m:return {"intent":"deposito"}
 return {"erro":"Operação não permitida"}