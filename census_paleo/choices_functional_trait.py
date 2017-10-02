CHOICES_HABITAT = (
    ("Forest", "Forest"),
    ("Heavy Cover", "Heavy Cover"),
    ("Light Cover", "Light Cover"),
    ("Grassland", "Grassland"),
)

CHOICES_BROWSEGRAZE = (
    ("Grazer", "Grazer"),
    ("Browser", "Browser"),
    ("Mixed Feeder", "Mixed Feeder"),
)

CHOICES_SIZE_LINTULAAKSO = (
    ("A", "A: 0.5 - 8 kg"),
    ("B", "B: 8 - 45 kg"),
    ("C", "C: 45 - 90 kg"),
    ("D", "D: 90 - 180 kg"),
    ("E", "E: 180 - 360 kg"),
    ("F", "F: 360 + kg"),
)

CHOICES_SIZE_BRAIN_BUNN = (
    ('1','I: < 23 kg',),
    ('2','II: 23 - 113 kg',),
    ('3','III: 113 - 340 kg',),
    ('4','IV: 340 - 907 kg',),
    ('5','V: 907 - 2721 kg'),
    ('6','VI: >2721 kg'),
)

CHOICES_LOCOMOTOR_REED = (
  ('A', 'arboreal'),
  ('AT','arboreal-terrestrial'),
  ('AQ','aquatic'),
  ('S','subterranean'),
  ('ST','subterranean-terrestrial'),
  ('T','terrestrial'),
  ('TA','terrestrial-aquatic'),
  )

CHOICES_TROPHIC_REED = (
    ("B","leaves"),
    ("C","meat"),
    ("C/B","meat/bone"),
    ("C/I","meat/invertebrates"),
    ("FG","fresh grass"),
    ("FL","fruit plus"),
    ("G","grass"),
    ("I","insects"),
    ("MF","leaves and grass"),
    ("OM","omnivorous"),
    ("R","roots/bulbs"),
)

CHOICES_TROPHIC_LINTULAAKSO = (
    ('C','Carnivore'),
    ('P','Piscivore'),
    ('M','Myrmecophage'),
    ('MF','Mixed-Feeder'),
    ('FG','Frugivore-Granivore'),
    ('FH','Frugivore-Herbivore'),
    ('FO','Frugivore-Omnivore'),
    ('IO','Insectivore-Omnivore'),
    ('I','Insectivore'),
    ('G','Grazer'),
    ('B','Browser'),
)

CHOICES_TROPHIC_ROWAN = (
    ("MF","Mixed-Feeder"),
    ("MF-B","Mixed-Feeder / Browser"),
    ("MF-FG","Mixed-Feeder / Frugivore-Granivore"),
    ("FG","Frugivore-Granivore"),
    ("MF-G","Mixed-Feeder / Grazer"),
    ("B","Browser"),
    ("OM","Omnivore"),
    ("C","Carnivore"),
    ("CI","Carnivore-Insectivore"),
    ("CB","Carnivore-Bone"),
    ("I","Insectivore"),
    ("G","Grazer"),
    ("FL","Fruit-Leaves"),
    ("FB","Fruit-Browse"),
    ("G-R","Grazer-Roots"),
    ("OM-FL","Omnivore-Fruit/Leaves"),
    ("OM-I","Omnivore-Insectivore"),
    ("OM-C","Omnivore-Carnivore"),
    ("FI","Fruit-Insects"),
    ("F","Fruit"),
    ("R","Roots"),
)

CHOICES_LOCOMOTOR_ROWAN = (
    ("T", "terrestrial"),
    ("AQ", "aquatic"),
    ("F", "fossorial"),
    ("A", "arboreal"),
    ("TA", "terrestrial-arboreal")
)