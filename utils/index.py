# import re
# target_str = """https://www.xiaohongshu.com/explore/666289f90000000015011be8?xsec_token=ABYhpT10B3SCS_ERbunw-avh7UNQQevWC7EQ2bB4zwIew=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/65f54ff8000000001202021e?xsec_token=AB87HzCLwNS7ptM-pXxRWgWRzGsVF85lT8lTJP3Xo_GX0=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/6633c49f000000001e01a814?xsec_token=ABXbgkn8TZ9SHsVK0xGvKp5Ijh7K-lc6YLS3hmkkjTVuc=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/6644e1b6000000001e02323a?xsec_token=ABASwV7sLD-dDZPKjkujUnt-3C-mrrPXVUpNTkokMnhTo=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/667fa302000000001c026dda?xsec_token=ABSbeOxkBuQ0eG-T_JLkCIQciktwevcMMWaxtpOxRqKQw=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/661ca62b000000001c008a26?xsec_token=ABsm-oxVsGw5RQAIN6iP6l3OdgmIRFO-_rHaJ-i2Sn3lU=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/6685517300000000030264f4?xsec_token=ABf7ea62ufFdoujBho88kEKiOZZeWIfP4Vf13eTOkgUy4=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/6629c153000000000401b418?xsec_token=ABtzkK6pRH1PvHAmru4ej5E4Bm6QN6dw5b3sJSI9sUTYs=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/66607ff5000000001500b279?xsec_token=ABJwYvcDRjqvKSuj8WcVPEC6aSp0MOQLJa-hNQgc5YsAU=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/6518f7a4000000001e03ee8b?xsec_token=AB3T3dVwjuVcdqN0MojUuB8WSOVQEruLApywed-e0ZgV0=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/666d5a7c000000001c021bc4?xsec_token=ABizGEVMKLB0FOQv1VTlWgSA2RviXjh-_s1WtUD5O9VkA=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/667cd085000000001c027d74?xsec_token=AB8dPvnM2eUfds69zbuIll5JAbllwwQCuEoiDiNc0PtaI=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/64f3c6b1000000001e03ff30?xsec_token=ABfnngKL3TcpRX3d2lPp17ke9yFVJzX0RotN3PnbtzFQ8=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/65f7e9b3000000000d00c239?xsec_token=ABML88wxdOpvJi_qM04jvsRs-siXSVhW8WRGBcdq4-u0s=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/651e2d48000000001a021bfe?xsec_token=ABtV-FKBGF_rtX_G8aKxz89qbfKY6DJh1PE-sKEsPOOU8=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/667a5b21000000001c037206?xsec_token=ABXJJg1VXXv0QKdoknJ1Udd-mr_I5s7ZNLbAXB-Tq7pSk=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/663fdb27000000001e037a99?xsec_token=ABYQt9VPztCrgyvi_AYtipTHPmlKvVyBaQBQ47f3Dn1-M=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/65bd22bf000000000201180c?xsec_token=AB7cslsPSLU2TErH48PJom36TtksWWoeRqfbod_9dgG8s=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/663a0d4a000000001e019dbb?xsec_token=AB3-XO45PG_WKIEZ3tRGrUag6LWnni37K_D_v9Qm8ISYw=&xsec_source=pc_search
# ,https://www.xiaohongshu.com/explore/668003f4000000001c0278c8?xsec_token=AB7mPgW1BwHNvxsznxQRlZCXI6rJ3ArSD_EHgdyxNzUZg=&xsec_source=pc_search]
# """

# test_str = 'https://www.xiaohongshu.com/explore/668003f4000000001c0278c8?xsec_token=AB7mPgW1BwHNvxsznxQRlZCXI6rJ3ArSD_EHgdyxNzUZg=&xsec_source=pc_search'
# pattern = r'https://www\\.xiaohongshu\\.com/explore.*'

# print(re.search(pattern,test_str),'结果')

# 测试log
