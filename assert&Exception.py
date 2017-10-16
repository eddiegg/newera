jinjiRoad = {"ns":"green","ew":"red"}
def traficLight(stopLight):
    for key in stopLight.keys():
        if stopLight[key] == "green":
            stopLight[key] = "yellow"
        elif stopLight[key] == "yellow":
            stopLight[key] = "red"
        elif stopLight[key] == "red":
            stopLight[key] = "green"
    assert "read" in stopLight.values(),"Neither light is read!"+str(stopLight)
traficLight(jinjiRoad)
print(jinjiRoad)