import mydict;

def test_dict_tem_campos():
  created_dict = mydict.create_dict()
  assert "nome" in created_dict, "O campo nome não consta no dicionário"
  assert "nota" in created_dict
  
def test_dict_campo_nome_eh_string():
    created_dict = mydict.create_dict()
    assert "nome" in created_dict and isinstance(created_dict["nome"], str)
