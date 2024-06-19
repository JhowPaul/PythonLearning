#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>


typedef struct 
{
    int codigo;
    char nome[200];
    struct
    {
        int dia;
        int mes;
        int ano;
    };
    
}Aluno;

Aluno aluno;

int main(void)

{

setlocale(LC_ALL,"portuguese");
aluno.codigo=0;
strcpy(aluno.nome,"NULL");
aluno.dia=0;
aluno.mes=0;
aluno.ano=0;
printf("\n O codigo do aluno e: %d",aluno.codigo);
printf("\n O nome do aluno e: %s",aluno.nome);
printf("\n A data de nascimento do aluno e: %d/%d/%d",aluno.dia,aluno.mes,aluno.ano);
printf("\n\n");
printf("\nDigite o codigo do aluno\n");
scanf("%d%*c",&aluno.codigo);
printf("\nDigite o nome do aluno\n");
scanf("%s%*c",&aluno.nome);
printf("\nDigite o dia de nascimento do aluno\n");
scanf("%d%*c",&aluno.dia);
printf("\nDigite o mes de nascimento do aluno\n");
scanf("%d%*c",&aluno.mes);
printf("\nDigite o ano de nascimento do aluno\n");
scanf("%d%*c",&aluno.ano);

printf("\n O codigo do aluno e: %d",aluno.codigo);
printf("\n O nome do aluno e: %s",aluno.nome);
printf("\n A data de nascimento do aluno e: %d/%d/%d",aluno.dia,aluno.mes,aluno.ano);
printf("\n\n");
system("PAUSE");

return(0);
}
