def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def sum_invalid_ids(input_line: str) -> int:
    total = 0
    ranges = input_line.strip().split(',')
    for r in ranges:
        start, end = map(int, r.split('-'))
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n

    return total



input_data = "3335355312-3335478020,62597156-62638027,94888325-95016472,4653-6357,54-79,1-19,314-423,472-650,217886-298699,58843645-58909745,2799-3721,150748-178674,9084373-9176707,1744-2691,17039821-17193560,2140045-2264792,743-1030,6666577818-6666739950,22946-32222,58933-81008,714665437-714803123,9972438-10023331,120068-142180,101-120,726684-913526,7575737649-7575766026,8200-11903,81-96,540949-687222,35704-54213,991404-1009392,335082-425865,196-268,3278941-3383621,915593-991111,32-47,431725-452205"

print(sum_invalid_ids(input_data))
