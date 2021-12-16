def solution(cache_size, cities):
    cache = []
    answer = 0
    for city in cities:
        city = city.lower()
        hit_index = 0
        if city in cache:
            answer += 1
            hit_index = cache.index(city)
        if city not in cache:
            answer += 5

        # cache_size == 0 인 case 때문에 pop & append
        cache.append(city)
        if len(cache) > cache_size:
            cache.pop(hit_index)

    return answer
