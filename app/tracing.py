# "OpenTelemetry provides distributed tracing for my FastAPI service. I configured a TracerProvider with the service name and used an OTLPSpanExporter to send traces to Tempo. FastAPIInstrumentor and SQLAlchemyInstrumentor automatically create spans for HTTP requests and database queries, so I don't need to add tracing code manually. A BatchSpanProcessor batches multiple spans before exporting them, which reduces network overhead and improves efficiency. actaully yeh 100 ko alag alag ki jd\gh ek sth bvhe deta hai"
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter



from opentelemetry.sdk.resources import Resource

def configure_tracing():
    resource = Resource(attributes={"service.name": "fastapi-app"})
    exporter = OTLPSpanExporter(endpoint="http://tempo:4317", insecure=True)    
    
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    
    trace.set_tracer_provider(provider)