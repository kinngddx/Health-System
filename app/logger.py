#yahan structlog configure karo JSON output ke liye  json format me likha jayeah easy to read understand the error

import structlog

# log.info("hello, %s!", "world", key="value!", more_than_strings=[1, 2, 3])
# 2022-10-07 10:41:29 [info     ] hello, world!   key=value! more_than_strings=[1, 2, 3]


#process chain hai jissse ki shi format me json data ko show kirega
structlog.configure(
    processors=[
       
        # structlog.processors.dict_tracebacks,
        structlog.processors.format_exc_info,    #exceptioon info ko readable format me convert krata hai 
        
        
        structlog.processors.TimeStamper(fmt="iso"),
        
       
        structlog.processors.add_log_level,
        
        #Aakhir mein pure data ko JSON bana do
        structlog.processors.JSONRenderer()
    ]
)


log = structlog.get_logger()