import paramiko

class node_manager:
    def __init__(self, ip, username, password):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, username=username, password=password)

    def no_hello(self):
        self.ssh.exec_command("sudo touch /no-hello")

    def set_hostname(self, name):
        self.ssh.exec_command("sudo sethostname {}".format(name))

    def reboot(self):
        self.ssh.exec_command("sudo reboot")

    def yes_hello(self):
        self.ssh.exec_command("sudo rm /no-hello")

    def set_password(self, password):
        self.ssh.exec_command("echo 'pi:{}' | sudo chpasswd".format(password))
        self.ssh.exec_command("echo 'root:{}' | sudo chpasswd".format(password))

    def update(self):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command("sudo apt update && sudo apt upgrade -y")
        #wait to complete
        ssh_stdout.read()

    def docker_install(self):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command("curl -sSL https://get.docker.com | sudo sh")
        #wait to complete
        ssh_stdout.read()

    def docker_setup_master(self, out_ip):
        self.ssh.exec_command("sudo usermod -aG docker pi")
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command("sudo docker swarm init --advertise-addr {}".format(out_ip))
        #wait to complete
        ssh_stdout.read()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command("sudo docker swarm join-token -q")
        return ssh_stdout.read()

    def docker_setup_worker(self, token, master_ip):
        self.ssh.exec_command("sudo docker swarm join --token {} {}:2377".format(token, master_ip))

    def docker_compose_install(self):
        self.ssh.exec_command("sudo apt-get install libffi-dev libssl-dev -y")
        self.ssh.exec_command("sudo apt-get install -y python python-pip -y")
        self.ssh.exec_command("sudo apt-get remove python-configparser -y")
        self.ssh.exec_command("sudo pip install docker-compose")