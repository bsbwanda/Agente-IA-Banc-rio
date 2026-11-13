from app.agents.intent_agent import detect
def test_bloqueio(): assert detect("bitcoin")["erro"]=="Operação não permitida"