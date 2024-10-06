from flask import Flask, request, jsonify
import whois
import dns.resolver

app = Flask(__name__)

@app.route('/api/domain-info', methods=['POST'])
def get_domain_info():
    data = request.json
    domain = data.get('domain')
    
    # WHOIS Lookup
    whois_info = whois.whois(domain)
    
    # DNS Lookup
    try:
        dns_info = dns.resolver.resolve(domain, 'A')
        ip_addresses = [ip.address for ip in dns_info]
    except Exception as e:
        ip_addresses = str(e)
    
    response = {
        'whois': str(whois_info),
        'ip_addresses': ip_addresses
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
