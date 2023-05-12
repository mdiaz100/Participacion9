from typing import Dict, Any

class AnalizadorLogs:
    def __init__(self, filename: str):
        self.filename = filename

    def analizar_logs(self) -> Dict[str, Any]:
        total_requests = 0
        http_method_stats = {}
        response_code_stats = {}
        total_response_size = 0
        url_stats = {}

        with open(self.filename, encoding="utf-8") as contenido:
            for line in contenido:
                try:
                    log_data = line.strip().split(' ')

                    ip_address, date_time, http_method, url, http_response_code, response_size = log_data

                    total_requests += 1

                    http_method_stats[http_method] = http_method_stats.get(http_method, 0) + 1

                    response_code_stats[http_response_code] = response_code_stats.get(http_response_code, 0) + 1

                    total_response_size += int(response_size)

                    url_stats[url] = url_stats.get(url, 0) + 1

                except ValueError:
                    print(f"Skipping line: {line.strip()}. Invalid format.")

        top_url_stats = sorted(url_stats.items(), reverse=True, key=lambda x: x[1])[:10]

        avg_response_size = total_response_size / total_requests

        return {
            "total_requests": total_requests,
            "http_method_stats": http_method_stats,
            "response_code_stats": response_code_stats,
            "total_response_size": total_response_size,
            "avg_response_size": avg_response_size,
            "top_url_stats": top_url_stats
        }


log_analyzer = AnalizadorLogs("trafico_web.log")
statistics_dict = log_analyzer.analizar_logs()
print(statistics_dict)
