from django.db import models

class GanhoDiario(models.Model):
    data = models.DateField(unique=True)
    receita = models.DecimalField(max_digits=8, decimal_places=2)
    ganho_por_km = models.DecimalField(max_digits=8, decimal_places=2)
    lucro = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Ganho Diário - {self.data}"


class GastoCombustivel(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    percurso = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Gasto Combustível - {self.data}"


class AluguelSemanal(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Aluguel Semanal - {self.data_inicio}"


class Meta(models.Model):
    meta_receita = models.DecimalField(max_digits=8, decimal_places=2)
    meta_ganho = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Meta"