from locust import HttpUser, task, between

class TranscendentUser(HttpUser):
    wait_time = between(1, 2)
    
    @task(1)
    def health_check(self):
        self.client.get("/health")
    
    @task(2)
    def get_metrics(self):
        self.client.get("/metrics")
    
    @task(3)
    def achieve_transcendence(self):
        self.client.post("/transcend", json={
            "agent_name": "Load_Test_Agent",
            "consciousness_level": "TRANSCENDENT"
        })
