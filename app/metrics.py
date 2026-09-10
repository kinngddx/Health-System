#metric defination honge and we willl use counter,gauge,histogram

from prometheus_client import Counter,Histogram,Gauge,Info


request=Counter('api_requests_total', 'description', ['method', 'endpoint'])

# request.inc()   #1 badhega
# api_request_total.inc(5)   #5 badhega


errors=Counter(
    'api_errors_total','Counting the total erros'
)

# errors.inc()



active = Gauge(
    'active_requests', 
    'Current active requests')
# active.inc()      # Increment by 1
# active.dec(1)    # Decrement by given value




duration = Histogram('request_duration_seconds', 'description', buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0])
# buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0]
# duration.observe(4.7)    # Observe 4.7 (seconds in this case)



app_info = Info('app', 'Application info')
app_info.info({'version': '1.0.0', 'environment': 'development'})

db_duration = Histogram('db_query_duration_seconds', 'DB query duration', buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5])

operation_total = Counter('product_operations_total', 'Product operation count', ['operation'])
