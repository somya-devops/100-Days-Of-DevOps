import random

# Simulating 3 backend application containers behind a Kubernetes Service
service_endpoints = {
    "pod-frontend-abc1": "10.244.1.45",
    "pod-frontend-xyz2": "10.244.2.89",
    "pod-frontend-lmn3": "10.244.1.92"
}

print("🔄 Kubernetes Service Routing: Checking active endpoints...")
print("=" * 60)

active_backends = []

for pod_name, pod_ip in service_endpoints.items():
    # Simulating a health check probe (randomly simulating a container failure)
    is_healthy = random.choice([True, True, False]) # 66% chance to be up
    
    if is_healthy:
        print(f"✅ [HEALTHY] Traffic routed to {pod_name} at IP: {pod_ip}")
        active_backends.append(pod_ip)
    else:
        print(f"❌ [UNHEALTHY] Pod {pod_name} failed probe. Removing from Service routing table.")

print("=" * 60)
print(f"📢 Active Load Balancer Target Group Pools: {active_backends}")