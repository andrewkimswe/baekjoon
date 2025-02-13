import sys
import heapq

def solve():
    input = sys.stdin.readline
    N, k = map(int, input().split())
    total_weighted_sum = 0
    cashier_heap = []
    finish_heap = []
    
    for i in range(N):
        customer_id, checkout_time = map(int, input().split())
        if len(cashier_heap) < k:
            heapq.heappush(cashier_heap, (checkout_time, i + 1, customer_id))
        else:
            finish_time, register_num, finished_customer = heapq.heappop(cashier_heap)
            heapq.heappush(finish_heap, (finish_time, -register_num, finished_customer))
            heapq.heappush(cashier_heap, (finish_time + checkout_time, register_num, customer_id))
    
    while cashier_heap:
        finish_time, register_num, finished_customer = heapq.heappop(cashier_heap)
        heapq.heappush(finish_heap, (finish_time, -register_num, finished_customer))
    
    order = 1
    while finish_heap:
        finish_time, neg_register, customer_id = heapq.heappop(finish_heap)
        total_weighted_sum += customer_id * order
        order += 1

    print(total_weighted_sum)

solve()