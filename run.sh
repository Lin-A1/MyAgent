#创建虚拟环境
conda create --name myagent python=3.10 -y

#进入虚拟环境
conda activate myagent

# cuda-11.8版本的gpu版torch
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 -f https://mirrors.aliyun.com/pytorch-wheels/cu118

# 安装依赖
pip install -e .

# 拉取mineru模型
pip install modelscope
wget https://gcore.jsdelivr.net/gh/opendatalab/MinerU@master/scripts/download_models.py -O download_models.py

# 进入download_models.py文件所在目录
cd scripts
python download_models.py