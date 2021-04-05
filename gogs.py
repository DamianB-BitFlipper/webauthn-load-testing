from locust import HttpUser, task, tag, constant_pacing, between
import sqlite3

class WebsiteUser(HttpUser):
    wait_time = constant_pacing(0.5)
    #wait_time = between(1, 3)

    def on_start(self):
        self.client.verify = False
        self.db = sqlite3.connect('../gogs/data/gogs.db')

    def repoCreate(self):
        self.client.post('/repo/create',
                         data='_csrf=st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA&user_id=1&repo_name=locust&description=&gitignores=&license=&readme=Default',
                         headers={
                             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
                             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                             "Accept-Language": "en-US,en;q=0.5",
                             "Content-Type": "application/x-www-form-urlencoded",
                         },

                         cookies={
                             "webauthn-session": "MTYxNzYzNDIzMXxEdi1CQkFFQ180SUFBUkFCRUFBQV9nR3hfNElBQWdaemRISnBibWNNRGdBTWNtVm5hWE4wY21GMGFXOXVCMXRkZFdsdWREZ0tjQUJ1ZXlKamFHRnNiR1Z1WjJVaU9pSnhUbVpPVmpneWJUQXlURFZuVWxFeVdrNVBWSEoxYXpaTVgxWklSbTE2Tkd0R1VVcHlXbTl2VTAxcklpd2lkWE5sY2w5cFpDSTZJa0ZSUVVGQlFVRkJRVUZCUVVGQlBUMGlMQ0oxYzJWeVZtVnlhV1pwWTJGMGFXOXVJam9pSW4wR2MzUnlhVzVuREJBQURtRjFkR2hsYm5ScFkyRjBhVzl1QjF0ZGRXbHVkRGdLX19nQV9fVjdJbU5vWVd4c1pXNW5aU0k2SWprMldWcGpTSEZFTm5sdVdXZEtTelE0VlRkdVdpMDFTRTlEYzJaUWRWQTJPSGg0TmpaeVRYUjRabU1pTENKMWMyVnlYMmxrSWpvaVFWRkJRVUZCUVVGQlFVRkJRVUU5UFNJc0ltRnNiRzkzWldSZlkzSmxaR1Z1ZEdsaGJITWlPbHNpVEU5WVNUTjRabWxNZGtsUU1EUk5SQzlUTWxwdFFUQk1aVmRMTlRsTVJtcEhaMHN3ZVRkVFQxb3pTQ3QzVHpOMWIwaDVTRll6WTJock9EQjVMM2hUVW0xQk9HNWFjVTFEWmtVMGEwdFdURzFsU21JMVZIbG5jRmRxWTJ4clREZzVjbU5ZUTNaWkx6WjZWbTg5SWwwc0luVnpaWEpXWlhKcFptbGpZWFJwYjI0aU9pSWlmUT09fPM5mxCP9cOjsL944xPOW4UsbPnQ-j9VaNdaFY3WB5xz",
                             "lang": "en-US",
                             "i_like_gogs": "ec3be125ff416d1c", 
                             "_csrf": "st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA",
                         },
        )

    @tag('repoDelete')
    @task
    def repoDelete(self):
        self.repoCreate()

        self.client.post('/damian/locust/settings',
                         data='-----------------------------28639370898985976491015983472\r\nContent-Disposition: form-data; name="_csrf"\r\n\r\nst48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA\r\n-----------------------------28639370898985976491015983472\r\nContent-Disposition: form-data; name="action"\r\n\r\ndelete\r\n-----------------------------28639370898985976491015983472\r\nContent-Disposition: form-data; name="repo_name"\r\n\r\nlocust\r\n-----------------------------28639370898985976491015983472\r\nContent-Disposition: form-data; name="auth_text"\r\n\r\nConfirm repository delete: damian/locust\r\n-----------------------------28639370898985976491015983472\r\nContent-Disposition: form-data; name="assertion"\r\n\r\n{"id":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","rawId":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","type":"public-key","response":{"authenticatorData":"SZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2MBAAAAAg","clientDataJSON":"eyJjaGFsbGVuZ2UiOiJxTUp6QjNBTEkxWlZibUxJLXJ2eTJsVHkzWFA0V1hIQUFDWEhCcDlNc1FrIiwiY2xpZW50RXh0ZW5zaW9ucyI6eyJ0eEF1dGhTaW1wbGUiOiJDb25maXJtIHJlcG9zaXRvcnkgZGVsZXRlOiBkYW1pYW4vbG9jdXN0In0sImhhc2hBbGdvcml0aG0iOiJTSEEtMjU2Iiwib3JpZ2luIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6ODA4MSIsInR5cGUiOiJ3ZWJhdXRobi5nZXQifQ","signature":"MEQCIHOAkg_nhy5QCCVOkdb96ym0y0YaSCf2eYwvO3wj_Y7uAiA7y0vSX2DCSF9TCYL1JQJnd2iBLaTuhnzAAgZGOA7z-Q"}}\r\n-----------------------------28639370898985976491015983472--\r\n',
                         headers={
                             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
                             "Accept": "*/*",
                             "Accept-Language": "en-US,en;q=0.5",
                             "Content-Type": "multipart/form-data; boundary=---------------------------28639370898985976491015983472",
                         },

                         cookies={
                             "webauthn-session": "MTYxNzYzNjUxMnxEdi1CQkFFQ180SUFBUkFCRUFBQV9nR3hfNElBQWdaemRISnBibWNNRUFBT1lYVjBhR1Z1ZEdsallYUnBiMjRIVzExMWFXNTBPQXJfLUFEXzlYc2lZMmhoYkd4bGJtZGxJam9pY1UxS2VrSXpRVXhKTVZwV1ltMU1TUzF5ZG5reWJGUjVNMWhRTkZkWVNFRkJRMWhJUW5BNVRYTlJheUlzSW5WelpYSmZhV1FpT2lKQlVVRkJRVUZCUVVGQlFVRkJRVDA5SWl3aVlXeHNiM2RsWkY5amNtVmtaVzUwYVdGc2N5STZXeUpNVDFoSk0zaG1hVXgyU1ZBd05FMUVMMU15V20xTU1VWlViSEZ1UTA5M1RXZFJkMEpFVmxGRVVXNU9Wa0Y1VEdOa09WbGhOalJTVWpSVE1FbzBPVU42U1V4QldYbFRlVEpPUmtGQmNsVjJZM2RJUkN0YVZsQnhWRFl4Y210WFJWTnhUMkZDTVcxR1IzSmtZejBpWFN3aWRYTmxjbFpsY21sbWFXTmhkR2x2YmlJNklpSjlCbk4wY21sdVp3d09BQXh5WldkcGMzUnlZWFJwYjI0SFcxMTFhVzUwT0Fwd0FHNTdJbU5vWVd4c1pXNW5aU0k2SWtFd1NrcFBTSE41WkhRemFteHhVMTlXY0RCWVptVnVXVWt3V25WeVMwUXhUMXB6TFVwc2EyZHdVa2tpTENKMWMyVnlYMmxrSWpvaVFWRkJRVUZCUVVGQlFVRkJRVUU5UFNJc0luVnpaWEpXWlhKcFptbGpZWFJwYjI0aU9pSWlmUT09fOclc4GTd0RDNSCY0dg1-52eWCf9H0OpBBBW9qnDYOrV",
                             "lang": "en-US",
                             "i_like_gogs": "ec3be125ff416d1c", 
                             "_csrf": "st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA",
                         },
        )

    @tag('addSSHKey')
    @task
    def addSSHKey(self):
        self.client.post('/user/settings/ssh',
                         data='-----------------------------28855191761370269280744625011\r\nContent-Disposition: form-data; name="_csrf"\r\n\r\nst48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA\r\n-----------------------------28855191761370269280744625011\r\nContent-Disposition: form-data; name="title"\r\n\r\nSlo\r\n-----------------------------28855191761370269280744625011\r\nContent-Disposition: form-data; name="content"\r\n\r\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDq1oWk52VynOu479FJh4xqw/y1jVpK+mOtKzFr8uKDg2rZO3Ip7/55raI0nnaupx7sWyqE8FR8EPLXLK1Nl+3Dhs/1EQaRlcVTcbC1GoYihTXfjtafgUgsCdUyq24/a1dD00yEGpjzTghNi4u20VmuDs136pVaaCDjsBwUAHeeM2WsASlTrVvzThVxpAc8LsgZItPYDtnl+3SiS05E89Ff1dPRKRl0vICjCyVthlNtUsyKq8bsLRoA7K3dsCNrrPhIqp7CZiF0R4ooRR5lqAoOOajXrXSWKhUrQC5tFcW0pk7aZfiDOamkVXaoZWEhYtOZ5KwJhGxaY+FN21/eKDQf/2guWMyLX0UPn4d1/eXFq1ATupzjEPkuMzqnseCShO2KwC20JgpfZxcQ2vcQK1SFlXT7XqpWRCZNVt/QdV21xb8ChdQKdJ7ql9R+xtOZN2JMrtqqdJVO4LmlGzoQ6bLi6ouoWYjwoqLacE3uqRkGbKgf6ThA6dVy32A6MnY2VQkYeHJxNPouUqHm2o3T6AwsSws4sjglSqEUamYezBVvWmrme/fADsc9SCe5gZWYMIH2s9KW+7ewnct+TIo0ucQdc1Adzq5vi7DbY50eZZdO/7HobKx/kddR75bsbmo6ZvcU524rEwrrkJIGQRABOGSUhYGWTLJDX8YK6un6APoyvQ== damianb@mit.edu\r\n-----------------------------28855191761370269280744625011\r\nContent-Disposition: form-data; name="auth_text"\r\n\r\nAdd SSH key named: Slo\r\n-----------------------------28855191761370269280744625011\r\nContent-Disposition: form-data; name="assertion"\r\n\r\n{"id":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","rawId":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","type":"public-key","response":{"authenticatorData":"SZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2MBAAAAAQ","clientDataJSON":"eyJjaGFsbGVuZ2UiOiItUlliS3lpcVh0c3BuSDdWbEtSR0ZPdkVUaldaXzByb0xLcVpaa051Z0RnIiwiY2xpZW50RXh0ZW5zaW9ucyI6eyJ0eEF1dGhTaW1wbGUiOiJBZGQgU1NIIGtleSBuYW1lZDogU2xvIn0sImhhc2hBbGdvcml0aG0iOiJTSEEtMjU2Iiwib3JpZ2luIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6ODA4MSIsInR5cGUiOiJ3ZWJhdXRobi5nZXQifQ","signature":"MEYCIQCmtDqrIovs6WADRuyE2vB_O1gSdwjtA6ZeVnYAV81fjwIhAKyqkKhkNdfyJa_GuWCOMzstjjL0bWsMdrv47uLFNw3I"}}\r\n-----------------------------28855191761370269280744625011--\r\n',
                         headers={
                             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
                             "Accept": "*/*",
                             "Accept-Language": "en-US,en;q=0.5",
                             "Content-Type": "multipart/form-data; boundary=---------------------------28855191761370269280744625011",
                         },

                         cookies={
                             "webauthn-session": "MTYxNzYzNjcyNXxEdi1CQkFFQ180SUFBUkFCRUFBQV9nR3hfNElBQWdaemRISnBibWNNRUFBT1lYVjBhR1Z1ZEdsallYUnBiMjRIVzExMWFXNTBPQXJfLUFEXzlYc2lZMmhoYkd4bGJtZGxJam9pTFZKWllrdDVhWEZZZEhOd2JrZzNWbXhMVWtkR1QzWkZWR3BYV2w4d2NtOU1TM0ZhV210T2RXZEVaeUlzSW5WelpYSmZhV1FpT2lKQlVVRkJRVUZCUVVGQlFVRkJRVDA5SWl3aVlXeHNiM2RsWkY5amNtVmtaVzUwYVdGc2N5STZXeUpNVDFoSk0zaG1hVXgyU1ZBd05FMUVMMU15V20xTU1VWlViSEZ1UTA5M1RXZFJkMEpFVmxGRVVXNU9Wa0Y1VEdOa09WbGhOalJTVWpSVE1FbzBPVU42U1V4QldYbFRlVEpPUmtGQmNsVjJZM2RJUkN0YVZsQnhWRFl4Y210WFJWTnhUMkZDTVcxR1IzSmtZejBpWFN3aWRYTmxjbFpsY21sbWFXTmhkR2x2YmlJNklpSjlCbk4wY21sdVp3d09BQXh5WldkcGMzUnlZWFJwYjI0SFcxMTFhVzUwT0Fwd0FHNTdJbU5vWVd4c1pXNW5aU0k2SWt0bmJHRklPVlU0V0hWNVRscE1URWxITjFkUWNVUkxYME5YVlVOUldUUkNkbU4xTUZKU1ZYVk1hR01pTENKMWMyVnlYMmxrSWpvaVFWRkJRVUZCUVVGQlFVRkJRVUU5UFNJc0luVnpaWEpXWlhKcFptbGpZWFJwYjI0aU9pSWlmUT09fD_-e6R-Q0-TYqVYYrx4ZjWFkOL7vkxUibQL-cwAKu6K",
                             "lang": "en-US",
                             "i_like_gogs": "ec3be125ff416d1c", 
                             "_csrf": "st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA",
                         },
        )

    @tag('deleteSSHKey')
    @task
    def deleteSSHKey(self):
        self.addSSHKey()

        # Change the ID of the new SSH key to 21 since delete only works on id=21
        self.db.execute('update public_key set id=142 where name="Slo";')
        self.db.commit()

        self.client.post('/user/settings/ssh/delete',
                         data='-----------------------------35060146163145915068482167655\r\nContent-Disposition: form-data; name="_csrf"\r\n\r\nst48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA\r\n-----------------------------35060146163145915068482167655\r\nContent-Disposition: form-data; name="id"\r\n\r\n142\r\n-----------------------------35060146163145915068482167655\r\nContent-Disposition: form-data; name="auth_text"\r\n\r\nDelete SSH key named: Slo\r\n-----------------------------35060146163145915068482167655\r\nContent-Disposition: form-data; name="assertion"\r\n\r\n{"id":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","rawId":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","type":"public-key","response":{"authenticatorData":"SZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2MBAAAAAg","clientDataJSON":"eyJjaGFsbGVuZ2UiOiIwNUJ3ZEpYTzl6RVVzbE1YdnlaYVRtUWN2WV9WZWZ5WHh2YmRFUVlpekY4IiwiY2xpZW50RXh0ZW5zaW9ucyI6eyJ0eEF1dGhTaW1wbGUiOiJEZWxldGUgU1NIIGtleSBuYW1lZDogU2xvIn0sImhhc2hBbGdvcml0aG0iOiJTSEEtMjU2Iiwib3JpZ2luIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6ODA4MSIsInR5cGUiOiJ3ZWJhdXRobi5nZXQifQ","signature":"MEYCIQDUS7i9chpkm3pFVrbGWKY9xzZ-3Aw19W1H1c9QK0J7EgIhALwAoVzzU5TCGe9Qccc1hcFP04I74iUwmQzbyTuoLHx4"}}\r\n-----------------------------35060146163145915068482167655--\r\n',
                         headers={
                             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
                             "Accept": "*/*",
                             "Accept-Language": "en-US,en;q=0.5",
                             "Content-Type": "multipart/form-data; boundary=---------------------------35060146163145915068482167655",
                         },

                         cookies={
                             "webauthn-session": "MTYxNzYzNjc4OXxEdi1CQkFFQ180SUFBUkFCRUFBQV9nR3hfNElBQWdaemRISnBibWNNRGdBTWNtVm5hWE4wY21GMGFXOXVCMXRkZFdsdWREZ0tjQUJ1ZXlKamFHRnNiR1Z1WjJVaU9pSkxaMnhoU0RsVk9GaDFlVTVhVEV4SlJ6ZFhVSEZFUzE5RFYxVkRVVmswUW5aamRUQlNVbFYxVEdoaklpd2lkWE5sY2w5cFpDSTZJa0ZSUVVGQlFVRkJRVUZCUVVGQlBUMGlMQ0oxYzJWeVZtVnlhV1pwWTJGMGFXOXVJam9pSW4wR2MzUnlhVzVuREJBQURtRjFkR2hsYm5ScFkyRjBhVzl1QjF0ZGRXbHVkRGdLX19nQV9fVjdJbU5vWVd4c1pXNW5aU0k2SWpBMVFuZGtTbGhQT1hwRlZYTnNUVmgyZVZwaFZHMVJZM1paWDFabFpubFllSFppWkVWUldXbDZSamdpTENKMWMyVnlYMmxrSWpvaVFWRkJRVUZCUVVGQlFVRkJRVUU5UFNJc0ltRnNiRzkzWldSZlkzSmxaR1Z1ZEdsaGJITWlPbHNpVEU5WVNUTjRabWxNZGtsUU1EUk5SQzlUTWxwdFRERkdWR3h4YmtOUGQwMW5VWGRDUkZaUlJGRnVUbFpCZVV4alpEbFpZVFkwVWxJMFV6QktORGxEZWtsTVFWbDVVM2t5VGtaQlFYSlZkbU4zU0VRcldsWlFjVlEyTVhKclYwVlRjVTloUWpGdFJrZHlaR005SWwwc0luVnpaWEpXWlhKcFptbGpZWFJwYjI0aU9pSWlmUT09fGbQqU7CE4lNYA1oP_1IH3y7ZeWO4YyAKh5kZYezifHQ",
                             "lang": "en-US",
                             "i_like_gogs": "ec3be125ff416d1c", 
                             "_csrf": "st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA",
                         },
        )

    @tag('settingsChangeEmail')
    @task
    def settingsChangeEmail(self):
        self.client.post('/user/settings', 
                         data='-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="_csrf"\r\n\r\nst48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="name"\r\n\r\ndamian\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="full_name"\r\n\r\n\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="email"\r\n\r\ntest@email.com\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="website"\r\n\r\n\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="location"\r\n\r\n\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="auth_text"\r\n\r\nConfirm profile details: username damian email test@email.com\r\n-----------------------------25729813608612628233745707030\r\nContent-Disposition: form-data; name="assertion"\r\n\r\n{"id":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","rawId":"LOXI3xfiLvIP04MD_S2ZmL1FTlqnCOwMgQwBDVQDQnNVAyLcd9Ya64RR4S0J49CzILAYySy2NFAArUvcwHD-ZVPqT61rkWESqOaB1mFGrdc","type":"public-key","response":{"authenticatorData":"SZYN5YgOjGh0NBcPZHZgW4_krrmihjLHmVzzuoMdl2MBAAAAAw","clientDataJSON":"eyJjaGFsbGVuZ2UiOiJLcUkyb0xmdG05ZHlsZWhtZUowa1M4WVE5aTBFVEZ5WW1vNlZCamdSQ2o0IiwiY2xpZW50RXh0ZW5zaW9ucyI6eyJ0eEF1dGhTaW1wbGUiOiJDb25maXJtIHByb2ZpbGUgZGV0YWlsczogdXNlcm5hbWUgZGFtaWFuIGVtYWlsIHRlc3RAZW1haWwuY29tIn0sImhhc2hBbGdvcml0aG0iOiJTSEEtMjU2Iiwib3JpZ2luIjoiaHR0cHM6Ly9sb2NhbGhvc3Q6ODA4MSIsInR5cGUiOiJ3ZWJhdXRobi5nZXQifQ","signature":"MEYCIQCU6qt64NXYvrpOcauB954HgeKLRH9NW2CN1Wjt99leHgIhAN43ri1muQjLxi4rgMHpXWf8aSTUhbRnGq95O2LAX9j4"}}\r\n-----------------------------25729813608612628233745707030--\r\n', 
                         headers={
                             "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
                             "Accept": "*/*",
                             "Accept-Language": "en-US,en;q=0.5",
                             "Content-Type": "multipart/form-data; boundary=---------------------------25729813608612628233745707030"
                         },
                         cookies={
                             "_csrf": "st48teqCv6sq03z6OSCqLGk538Q6MTYxNzU1OTA3ODc2OTkyNTkxNA",
                             "lang": "en-US",
                             "i_like_gogs": "ec3be125ff416d1c",
                             "webauthn-session": "MTYxNzYzNjk0NXxEdi1CQkFFQ180SUFBUkFCRUFBQV9nR3hfNElBQWdaemRISnBibWNNRGdBTWNtVm5hWE4wY21GMGFXOXVCMXRkZFdsdWREZ0tjQUJ1ZXlKamFHRnNiR1Z1WjJVaU9pSkxaMnhoU0RsVk9GaDFlVTVhVEV4SlJ6ZFhVSEZFUzE5RFYxVkRVVmswUW5aamRUQlNVbFYxVEdoaklpd2lkWE5sY2w5cFpDSTZJa0ZSUVVGQlFVRkJRVUZCUVVGQlBUMGlMQ0oxYzJWeVZtVnlhV1pwWTJGMGFXOXVJam9pSW4wR2MzUnlhVzVuREJBQURtRjFkR2hsYm5ScFkyRjBhVzl1QjF0ZGRXbHVkRGdLX19nQV9fVjdJbU5vWVd4c1pXNW5aU0k2SWt0eFNUSnZUR1owYlRsa2VXeGxhRzFsU2pCclV6aFpVVGxwTUVWVVJubFpiVzgyVmtKcVoxSkRhalFpTENKMWMyVnlYMmxrSWpvaVFWRkJRVUZCUVVGQlFVRkJRVUU5UFNJc0ltRnNiRzkzWldSZlkzSmxaR1Z1ZEdsaGJITWlPbHNpVEU5WVNUTjRabWxNZGtsUU1EUk5SQzlUTWxwdFRERkdWR3h4YmtOUGQwMW5VWGRDUkZaUlJGRnVUbFpCZVV4alpEbFpZVFkwVWxJMFV6QktORGxEZWtsTVFWbDVVM2t5VGtaQlFYSlZkbU4zU0VRcldsWlFjVlEyTVhKclYwVlRjVTloUWpGdFJrZHlaR005SWwwc0luVnpaWEpXWlhKcFptbGpZWFJwYjI0aU9pSWlmUT09fN8dzZ13MZ1unHqZj8gq0aRLTNcIazFMyH4JUFfrMtQz",
                         }
        )
