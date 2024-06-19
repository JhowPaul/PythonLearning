#include <stdio.h>

//Salario
void Salario() {
	int salario,media,somar,maior,i,x;
	media = 0, somar=0,maior=0;
	for (x=1,i = 0; x<10,i < 10;x++, i++)
	{
		printf("Digite o seu salario %d: ",x);
		scanf_s("%d", &salario);
		somar += salario;

		if (salario > maior)
			maior = salario;

		
		
	}
	media=(somar)/i;
	printf("A media dos salarios e: %.1d", media);

}


//Reajuste salarial
void Reajuste() {
	float salario, reajustSalario = 0, maiorSal = 0,salReaj=0;
	
	
	
	printf("Insira a porcentagem de reajuste salarial: ");
	scanf_s("%f", &reajustSalario);

	for (int i = 0; i < 5; i++)
	{
		
		printf("Insira o seu salario: ");
		scanf_s("%f", &salario);
		
		salReaj = salario + (salario*reajustSalario/100);
		printf("O seu Salario reajustado e: %.2f \n", salReaj);

		if (salReaj>maiorSal)
		{
			maiorSal = salReaj;
		}
		

	}
	printf("O maior salario reajustado e: %.2f \n", maiorSal);
}


void Numero() {

	int numero,num,somaPar=0,somaImpar=0;

	printf("Insira o numero de vezes a se repetir: ");
	scanf_s("%d", &numero);

	for (int i = 0; i < numero; i++)
	{
		printf("Insira um numero: ");
		scanf_s("%d", &num);

		if (num%2==0)
		{
			somaPar += num;
		}
		else
		{
			somaImpar += num;
		}

	}
	printf("A soma dos numeros pares e : %d\n", somaPar);
	printf("A soma dos numeros impares e : %d \n", somaImpar);
}


//Nota
void Nota() {
	int nota1=0, nota2 = 0, nota3 = 0, media=0;

	for (int i = 0;i < 6; i++)
	{
		printf("Digite a 1 nota: ");
		scanf_s("%d", &nota1);
		printf("Digite a 2 nota: ");
		scanf_s("%d", &nota2);
		printf("Digite a 3 nota: ");
		scanf_s("%d", &nota3);
		media = (nota1+nota2+nota3)/3;

		if (media>=7)
		{
			printf("media %d Aprovado\n",media);
		}
		else
		{
			printf("media %d Reproved\n", media);
		}
	}
	


}


int main() {
	int soma=0;
	int media = 0;
	Numero();
	Reajuste();
	Nota();
	Salario();

	for (int i = 0; i <= 10; i++)
	{
		printf("%d\n", i);
	}
	for (int i = 10; i >= 0; i--)
	{
		printf("%d\n", i);
	}

	for (int i = 0; i <= 10; i += 2)
	{
		printf("%d\n", i);
	}

	for (int i = 0; i <= 100; i += 10)
	{
		printf("%d\n", i);
	}

	for (int i = 100; i >= 0; i -= 10)
	{
		printf("%d\n", i);
	}

	for (int i = 1000; i >=100 ; i-=100)
	{
		printf("%d\n", i);
	}

	for (int i = 0; i <= 10; i++)
	{
		soma += i;
	}
	printf("%d\n",soma);

	for (int i = 0; i <= 10; i++)
	{
		soma += i;
	}
	media = soma / 10;
	printf("%d\n", media);

	int numero;

	printf("Insira um numero: ");
	scanf_s("%d", &numero);

	for (int x=0, i = 0; x,i < 20; x++, i++)
	{
		printf("%d: %d\n", x,numero);
	}
	int n, maior;
	maior = 0;
	for (int i = 0; i < 15; i++)
	{
		printf("Digite um numero: ");
		scanf_s("%d", &n);

		if (n>maior)
		{
			maior = n;
		}
		


	}
	printf("%d", maior);




}





