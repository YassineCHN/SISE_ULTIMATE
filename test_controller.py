"""
Diagnostic manette — affiche axes et boutons en temps réel.
Usage : uv run test_controller.py
Appuie sur Ctrl+C pour quitter.
"""
import pygame
import time
import os

pygame.init()
pygame.joystick.init()

count = pygame.joystick.get_count()
if count == 0:
    print("❌ Aucune manette détectée.")
    raise SystemExit

joy = pygame.joystick.Joystick(0)
joy.init()
print(f"\n🎮 Manette : {joy.get_name()}")
print(f"   Axes    : {joy.get_numaxes()}")
print(f"   Boutons : {joy.get_numbuttons()}")
print(f"   Hats    : {joy.get_numhats()}")
print("\nBouge les joysticks et appuie sur les boutons...\n")

try:
    while True:
        pygame.event.pump()

        axes = [round(joy.get_axis(i), 2) for i in range(joy.get_numaxes())]
        btns = [i for i in range(joy.get_numbuttons()) if joy.get_button(i)]

        os.system("cls" if os.name == "nt" else "clear")
        print(f"🎮 {joy.get_name()}\n")
        print("AXES :")
        for i, v in enumerate(axes):
            bar = "█" * int(abs(v) * 20)
            sign = "+" if v >= 0 else "-"
            print(f"  Axe {i:2d} : {sign}{bar:<20} {v:+.2f}")
        print(f"\nBOUTONS PRESSÉS : {btns if btns else 'aucun'}")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nFin du diagnostic.")
    pygame.quit()
