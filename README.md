# TibSenCorpus

A Tibetan-Chinese parallel corpus for five-level sensitive content grading (S0-S4).

The release contains **157,527 records** with Chinese text, Tibetan translation, topic, special tag, dissemination channel, and sensitivity label. Original sample identifiers are retained and may be non-consecutive. Workbook column names and label counts are documented in [dataset_metadata.json](dataset_metadata.json).

## Data access

TibSenCorpus is provided for **non-commercial research only**. The workbook is distributed as a password-protected 7z archive because it contains sensitive content. The password and unencrypted data are not published in this repository.

1. Download all three encrypted archive volumes to the same directory:
   [Part 1](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.001),
   [Part 2](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.002), and
   [Part 3](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.003).
2. Read [DATA_ACCESS.md](DATA_ACCESS.md).
3. Email **cvlina@mail.nwpu.edu.cn**, preferably from your institutional email address, with the subject **TibSenCorpus Data Access Request**. Include your name, affiliation, intended research use, and confirmation that you agree to the non-commercial research access terms.
4. The dataset maintainer reviews the request and sends the extraction password by email if access is approved.

Suggested email:

```text
Subject: TibSenCorpus Data Access Request

Name:
Affiliation:
Institutional email:
Intended research use:

I have read DATA_ACCESS.md and agree to use TibSenCorpus only for
non-commercial research. I will not redistribute the data or the
extraction password, or use the dataset for commercial purposes.
```

Please do not post access requests containing personal details or share the password in public issues. This repository does not automatically send email replies or grant access.

## Integrity and extraction

Compare the downloaded volumes' SHA-256 values with [SHA256SUMS.txt](SHA256SUMS.txt) before extraction. Keep all three volumes together, open the `.7z.001` file in 7-Zip or another compatible application, and enter the password supplied by the maintainer. The archive uses AES-256 encryption and also encrypts filenames.

Alternatively, [download_dataset.py](download_dataset.py) downloads, verifies, and joins the volumes into one encrypted `.7z` file. It uses only the Python standard library and does not require or contain the extraction password:

```bash
python download_dataset.py --output-dir TibSenCorpus_download
```

The release preserves the confirmed final workbook without altering its contents. No training checkpoints or test results are included in this data release.

## Access-policy references

The access workflow follows established dataset-sharing practices: [DocTamper](https://github.com/qcf-568/DocTamper) uses non-commercial access with email password requests; [VisualSem](https://github.com/iacercalixto/visualsem) distributes password-protected data with institutional-email requests; and [FERV39k](https://github.com/wangyanckxx/FERV39k) requests researcher information and non-commercial-use commitments. Their dataset-specific licences are not copied or applied to TibSenCorpus.

## 中文说明

本数据集仅供非商业学术研究使用。请下载加密压缩包，并向 **cvlina@mail.nwpu.edu.cn** 发送申请邮件，说明姓名、单位、研究用途，并确认遵守 [数据获取与使用条款](DATA_ACCESS.md)。审核通过后，维护者将通过邮件提供解压密码。请勿公开传播明文数据或密码。
