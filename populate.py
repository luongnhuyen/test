import mlab
from models.service import Service

mlab.connect()

service = Service(name="Chè thái sầu riêng tươi",
             type="food",
             price=28000,
             link="https://www.now.vn/ha-noi/co-lien-che-da-nang",
             picture="https://media.foody.vn/res/g20/193679/s600x600/201682173441-che-thai-sau-rieng-tuoi.jpg")
service.save()
