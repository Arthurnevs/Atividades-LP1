conta = (input())

soma = 0
for x in conta:
	soma = int(x) + soma

print('{}-{:02d}'.format(conta,soma%11))

