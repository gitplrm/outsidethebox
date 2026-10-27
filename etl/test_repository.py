from repository.turma_repository import (
    get_media_por_turma,
    get_ranking_turmas,
    get_media_por_disciplina
)

print("\nMEDIA POR TURMA")
print(
    get_media_por_turma()
)

print("\nRANKING")
print(
    get_ranking_turmas()
)

print("\nDISCIPLINAS")
print(
    get_media_por_disciplina()
)