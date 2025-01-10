def solution(hp):
    general = 5
    soldier = 3
    worker = 1

    generals = hp // general
    remaining_hp = hp % general

    soldiers = remaining_hp // soldier
    remaining_hp %= soldier

    workers = remaining_hp // worker

    return generals + soldiers + workers