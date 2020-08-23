import unittest
from .utils import swp_lng

class MyTestCase(unittest.TestCase):
    def test_swp_lng_1(self):
        self.assertEqual(swp_lng('ghbdtn'), 'привет')

    def test_swp_lng_2(self):
        self.assertEqual(swp_lng('привет'), 'ghbdtn')

    def test_swp_lng_3(self):
        self.assertEqual(swp_lng('ghbdtn rfr ltkf e nt,z'), 'привет как дела у тебя')

    def test_swp_lng_4(self):
        self.assertEqual(swp_lng('Ghbdtn Vbh ```'), 'Привет Мир ```')

    def test_swp_lng_5(self):
        self.assertEqual(swp_lng('Vj;yj rjytxyj gthtgtxfnfnm? f xnj ltkfnm tckb ntrcnf yf,hfyj vyjuj? ' \
                  'bkb dfv ghbckfkb cjj,otybt yf,hfyyjt ' \
                  'yt d njq hfcrkflrt'), 'Можно конечно перепечатать, а что делать если текста набрано много, ' \
                                      'или вам прислали сообщение набранное не в той раскладке')

    def test_swp_lng_6(self):
        self.assertEqual(swp_lng('Случайно забыли переключить язык и набрали текст не в той раскладке и на выходе ' \
                  'получили непонятный набор букв'), 'Ckexfqyj pf,skb gthtrk.xbnm zpsr b yf,hfkb ntrcn yt d njq ' \
                                      'hfcrkflrt b yf ds[jlt gjkexbkb ytgjyznysq yf,jh ,erd')

    def test_swp_lng_7(self):
        self.assertEqual(swp_lng('похожие на "Ghbdtn? rfr ltkf vjq lheu&"? Можно конечно перепечатать'), 'gj[j;bt yf "Ghbdtn? rfr ltkf vjq lheu&"? Vj;yj rjytxyj gthtgtxfnfnm')

    def test_swp_lng_8(self):
        self.assertEqual(swp_lng(''), 'Error')

    def test_swp_lng_9(self):
        self.assertEqual(swp_lng('   '), '   ')


if __name__ == '__main__':
    unittest.main()
