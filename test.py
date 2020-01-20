import ClassesBackpack as Cl

print(Cl.Canteen.full)

Cl.Canteen = Cl.Healing("Canteen", "full", 25, "A canteen that is full of water")

print(Cl.Canteen.full)
