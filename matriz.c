#include<stdio.h>

void Nota() {

	int nota[3][100];

	for (int i = 0; i < 3; i++)
	{
		for (int k = 0; k < 100; k++)
		{
			nota[i][k] = 0;
			printf("%d", nota[i][k]);
		}

	}

}

void Teste() {
	int num[3][4], i, k, par = 0, impar = 0;

	printf("Digite uma sequencia de numeros\n");

	for (i = 0; i < 3; i++) {
		for (k = 0; k < 4; k++) {
			printf("Elemento[%d][%d]", i, k);
			scanf_s("%d", &num[i][k]);


		}

	}
	printf("\nBi boboboro bo\n");
	for (i = 0; i < 3; i++) {
		for (k = 0; k < 4; k++) {
			if (num[i][k] % 2 == 0) {
				par++;
			}
			else {
				impar++;
			}
		}

	}
	printf("Indices pares: %d\n", par);
	printf("Indices impares: %d\n", impar);
}

void Ar() {
	int matriz[4][4], i, k;

	printf("Digite uma sequencia:\n");
	for (i = 0; i < 4; i++) {
		//matriz[i]=0
		for (k = 0; k < 4; k++) {
			//  scanf("%d",&matriz[k]);
			if (i == k) {
				matriz[i][k] = 0;
				printf("Elemento[%d][%d]= 0\n", i, k);
			}
			else {
				printf("Elemento[%d][%d]= ", i, k);
				scanf_s("%d", &matriz[i][k]);
			}
		}
	}
	printf("\n\nExibicao\n\n");
	for (i = 0; i < 4; i++) {

		for (k = 0; k < 4; k++) {
			printf(" %d ", matriz[i][k]);
		}
		printf("\n");
	}
}

void Invert() {
	int matriz[4][4], i, k, neji[4][4];

	printf("Insira um numero: \n");

	for (i = 0; i < 4; i++) {
		for (k = 0; k < 4; k++) {
			printf("Elemento [%d][%d]: ", i, k);
			scanf_s("%d", &matriz[i][k]);
			neji[k][i] = matriz[i][k];
		}
	}
	printf("\n\nTexto\n\n");

	for (i = 0; i < 4; i++)
	{
		for (k = 0; k < 4; k++)
		{
			
			printf("%d ",neji[i][k]);
			
		}
		printf("\n");
	}
}

void Maior() {
	int matriz[3][3], maior = 0, i, k;

	printf("Digite um numero: ");
	for (i = 0; i < 3; i++) {
		for (k = 0; k < 3; k++) {
			scanf_s("%d", &matriz[i][k]);
			if (matriz[i][k] > maior) {
				maior = matriz[i][k];

			}
			if (maior == matriz[i][k]) {
				printf("%d", maior);
			}
		}
	}

}

void ZeroUm() {
	int matriz[5][5], i, k;

	for (i = 0; i < 5; i++) {
		for (k = 0; k < 5; k++) {
			matriz[i][k] = 1;
			if (i == k) {
				matriz[i][k] = 0;

			}
			printf(" %d", matriz[i][k]);
		}
		printf("\n");

	}
}



int main() {
	
	
	ZeroUm();
	Maior();
	Ar();
	Invert();
	Teste();
	Nota();
	return 0;
}