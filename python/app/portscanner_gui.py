from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, 
                             QLineEdit, QTextEdit, QWidget, QFileDialog, QProgressBar)
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import socket
import csv
import json

class PortScannerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KN8T")
        self.setGeometry(300, 200, 700, 500)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)


        self.target_label = QLabel("Hedef IP (virgülle ayırarak birden fazla girebilirsiniz):")
        self.layout.addWidget(self.target_label)
        self.target_input = QLineEdit()
        self.layout.addWidget(self.target_input)

 
        self.port_label = QLabel("Port Aralığı (örn: 20-80):")
        self.layout.addWidget(self.port_label)
        self.port_input = QLineEdit()
        self.layout.addWidget(self.port_input)


        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.layout.addWidget(self.result_box)


        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.start_button = QPushButton("Taramayı Başlat")
        self.layout.addWidget(self.start_button)
        self.stop_button = QPushButton("Taramayı Durdur")
        self.stop_button.setDisabled(True)
        self.layout.addWidget(self.stop_button)


        self.save_button = QPushButton("Sonuçları Kaydet")
        self.save_button.setDisabled(True)
        self.layout.addWidget(self.save_button)

        self.start_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.stop_scan)
        self.save_button.clicked.connect(self.save_results)

        self.thread = None
        self.scan_results = []

    def start_scan(self):
        target = self.target_input.text()
        port_range = self.port_input.text()

        if not target or not port_range or '-' not in port_range:
            self.result_box.append("Lütfen geçerli bir hedef ve port aralığı girin.")
            return

        try:
            start_port, end_port = map(int, port_range.split('-'))
        except ValueError:
            self.result_box.append("Port aralığı düzgün bir şekilde girilmelidir (örn: 20-80).")
            return

        targets = target.split(',')
        self.result_box.append(f"Taramaya başlandı: {targets}, Portlar: {start_port}-{end_port}")
        self.progress_bar.setMaximum(len(targets) * (end_port - start_port + 1))
        self.progress_bar.setValue(0)

        self.thread = PortScanThread(targets, range(start_port, end_port + 1))
        self.thread.result_signal.connect(self.update_results)
        self.thread.progress_signal.connect(self.update_progress)
        self.thread.finished_signal.connect(self.scan_finished)
        self.thread.start()

        self.start_button.setDisabled(True)
        self.stop_button.setEnabled(True)

    def stop_scan(self):
        if self.thread and self.thread.isRunning():
            self.thread.terminate()
            self.result_box.append("Tarama durduruldu!")
            self.start_button.setEnabled(True)
            self.stop_button.setDisabled(True)

    def save_results(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Sonuçları Kaydet", "", "JSON Dosyası (*.json);;CSV Dosyası (*.csv)")
        if file_path:
            if file_path.endswith('.json'):
                with open(file_path, 'w') as file:
                    json.dump(self.scan_results, file, indent=4)
            elif file_path.endswith('.csv'):
                with open(file_path, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Hedef", "Port", "Durum"])
                    writer.writerows(self.scan_results)
            self.result_box.append(f"Sonuçlar kaydedildi: {file_path}")

    def update_results(self, result):
        self.result_box.append(result)
        target, port, status = result.split()
        self.scan_results.append((target, port, status))

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def scan_finished(self):
        self.result_box.append("Tarama tamamlandı!")
        self.start_button.setEnabled(True)
        self.stop_button.setDisabled(True)
        self.save_button.setEnabled(True)


class PortScanThread(QThread):
    result_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self, targets, ports):
        super().__init__()
        self.targets = targets
        self.ports = ports

    def run(self):
        total_tasks = len(self.targets) * len(self.ports)
        completed_tasks = 0

        for target in self.targets:
            for port in self.ports:
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)
                        result = s.connect_ex((target.strip(), port))
                        status = "Açık" if result == 0 else "Kapalı"
                        self.result_signal.emit(f"{target} {port} {status}")
                except Exception as e:
                    self.result_signal.emit(f"{target} {port} Hata: {e}")
                completed_tasks += 1
                self.progress_signal.emit(completed_tasks)

        self.finished_signal.emit()





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    gui = PortScannerGUI()
    gui.show()
    sys.exit(app.exec_())