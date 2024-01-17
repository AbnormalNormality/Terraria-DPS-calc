import random
import time
import msvcrt
def finddps(stats,buffs,defense):
    global useTime
    damage, useTime, critChance = map(int, stats.split(","))
    if not buffs == "":
        damageBuff, useTimeBuff, critChanceBuff = map(int, buffs.split(","))
        damage = damage + (damageBuff / 100) * damage
        useTime = useTime + (useTimeBuff / 100) * useTime
        critChance = critChance + (critChanceBuff / 100) * critChance
    if not defense == "":
        defense = int(defense)
        defense = defense / 2
    else:
        defense = 0
    x = 0
    dps = 0
    while x < 60:
        hit = 0
        hit += round(damage * random.randint(85, 115) / 100)
        crit = random.randint(1, 100)
        if crit <= critChance:
            hit *= 2
        hit -= defense
        if hit < 1:
            hit = 1
        dps += hit
        x += useTime
        if useTime == 0:
            break
    return dps
stats = input("What is the base damage, use time, and critical hit chance of the weapon seperated by commas?\n")
buffs = input("What damage, use time, and critical hit chance modifiers do you have seperated by commas? Leave blank for none\n")
subStats = input("If your weapons produces sub projectiles, what is the base damage, use time, and critical hit chance of the projectiles seperated by commas? Leave blank for none\n")
if not subStats == "":
    subBuffs = input("What damage, use time, and critical hit chance modifiers do the projectiles have seperated by commas? Leave blank for none\n")
defense = input("What is the defense of the enemy? Leave blank for none\n")
dps = 0
max = 0
min = 0
while not msvcrt.kbhit() or msvcrt.getch() != b'\r':
    if subStats == "":
        dps = finddps(stats,buffs,defense)
    else:
        dps = finddps(stats,buffs,defense) + finddps(subStats, subBuffs, defense)
    if dps > max:
        max = dps
    if dps < min or min == 0:
        min = dps
    print(dps)
    time.sleep(useTime / 60)
    print("\033[A                             \033[A")

print(min,"-",max)
input("Press ENTER to exit")