# TibSenCorpus

A Tibetan-Chinese parallel corpus for five-level sensitive content grading (S0-S4).

The release contains **157,527 records** with Chinese text, Tibetan translation, topic, special tag, dissemination channel, and sensitivity label. Original sample identifiers are retained and may be non-consecutive. Workbook column names and label counts are documented in [dataset_metadata.json](dataset_metadata.json).

## Data access

TibSenCorpus is provided for **non-commercial research only**. The workbook is distributed as a password-protected 7z archive because it contains sensitive content. The password and unencrypted data are not published in this repository.

1. Read [DATA_ACCESS.md](DATA_ACCESS.md) and download the blank
   [Dataset Release Agreement (PDF)](agreements/TibSenCorpus_Dataset_Release_Agreement.pdf).
2. Complete the simple information table (name, organization, position, institutional email,
   and one shared homepage field), print the one-page form, and **sign by hand**.
   Student applicants must also obtain their supervisor's or principal investigator's signature.
3. Scan the complete signed page into one legible PDF and email it to **cvlina@mail.nwpu.edu.cn** from
   your institutional email address, with the subject **TibSenCorpus Data Access Request**.
   If you do not have an institutional address, contact the maintainer before submitting.
   **Do not upload signed agreements to public GitHub issues, pull requests, or commits.**
4. The dataset maintainer reviews the signed application and sends the extraction password by email
   if access is approved. An email-only promise without the signed agreement is not a complete application.
5. Download all three encrypted archive volumes to the same directory:
   [Part 1](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.001),
   [Part 2](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.002), and
   [Part 3](https://raw.githubusercontent.com/cvNXE/TibSenCorpus/main/data/TibSenCorpus_S0-S4_v1.0.0.7z.003).

Suggested email:

```text
Subject: TibSenCorpus Data Access Request

Please find attached my completed and hand-signed TibSenCorpus Dataset
Release Agreement (one page). I request access for non-commercial research.

Attachment: TibSenCorpus_Agreement_[ApplicantName].pdf
```

Please do not post access requests containing personal details or share the password in public issues. This repository does not automatically send email replies or grant access.

The black-and-white, single-page agreement has fillable information fields and blank handwritten-signature lines.
An [editable text version](agreements/TibSenCorpus_Dataset_Release_Agreement.md) and
[PDF-generation script](scripts/build_agreement.py) are also provided. Signatures must be supplied
by the actual applicant and, for students, the supervisor/PI; no signatures are prefilled.

## Integrity and extraction

Compare the downloaded volumes' SHA-256 values with [SHA256SUMS.txt](SHA256SUMS.txt) before extraction. Keep all three volumes together, open the `.7z.001` file in 7-Zip or another compatible application, and enter the password supplied by the maintainer. The archive uses AES-256 encryption and also encrypts filenames.

Alternatively, [download_dataset.py](download_dataset.py) downloads, verifies, and joins the volumes into one encrypted `.7z` file. It uses only the Python standard library and does not require or contain the extraction password:

```bash
python download_dataset.py --output-dir TibSenCorpus_download
```

The release preserves the confirmed final workbook without altering its contents. No training checkpoints or test results are included in this data release.

## Access-policy references

The signed-application workflow is informed by the public
[SUSTech1K release agreement](https://lidargait.github.io/static/resources/SUSTech1KAgreement.pdf)
and [EPHOIE access procedure](https://github.com/HCIILAB/EPHOIE). Non-commercial email/password
access is also documented by [DocTamper](https://github.com/qcf-568/DocTamper) and
[VisualSem](https://github.com/iacercalixto/visualsem). These references inform the workflow;
their dataset-specific licences, institutional claims, and signed personal information are not
copied or applied to TibSenCorpus.

## 中文说明

本数据集仅供非商业学术研究使用。申请人须下载并填写 [黑白单页使用协议](agreements/TibSenCorpus_Dataset_Release_Agreement.pdf)，打印后亲笔签名；学生申请人还须由导师或项目负责人签名。将签署后的完整一页扫描为 PDF，以邮件附件发送至 **cvlina@mail.nwpu.edu.cn**，审核通过后获取解压密码。仅发送邮件承诺不能替代签署协议。签署后的协议含个人信息和签名，**请勿上传公开 GitHub 仓库或 Issue**。明文数据和密码同样不得公开传播。
