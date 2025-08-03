for i in range(1, 19):
    print(f'''    if bool(data["TeamInfo"]["Score"]["{i}"]["Valid"]): team.hole{i} = data["TeamInfo"]["Score"]["{i}"]["RawScore"]''')
