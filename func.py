conv={"привет":"И тебе привет!", "как дела":"Лучше всех", "пока":"Увидимся"}

def get_answer(key,dialog):
	c=key.lower()
	b=dialog.get(c)
	return b

a=input("")
print(get_answer(a,conv))