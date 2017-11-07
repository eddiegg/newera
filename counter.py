from collections import Counter
sampleStr = "asf dasdbvpasdpqfg"
print(dict(Counter(sampleStr.split()).most_common())["asf"])