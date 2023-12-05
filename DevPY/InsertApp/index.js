import moment from 'moment'

import formatData from './format-data.js'

let module = {}
module.formatDate = (dateN, pattern = 'YYYY年MM月DD日') => {
  // return (dateN !== void 0 && dateN !== null) ? dateFormat(dateN, 'YYYY[年]MM[月]DD[日]') : ''
  return (dateN !== void 0 && dateN !== null) ?
    moment(dateN).format(pattern) : ''
}

module.formatTS = (dateN) => {
  // return (dateN !== void 0 && dateN !== null) ? dateFormat(dateN, 'YYYY[年]MM[月]DD[日]HH[时]mm[分]ss[秒]') : ''
  return (dateN !== void 0 && dateN !== null) ?
    moment(dateN).format('YYYY年MM月DD日HH时mm分ss秒') : ''
}

module.formatTSShort = (dateN) => {
  return (dateN !== void 0 && dateN !== null) ?
    moment(dateN).format('YYYY年MM月DD日 HH:mm:ss') : ''
}

module.formatTSShortEn = (dateN) => {
  return (dateN !== void 0 && dateN !== null) ?
    moment(dateN).format('YYYY/MM/DD HH:mm:ss') : ''
}

module.ab2hex = (buffer) => {
  const hexArr = Array.prototype.map.call(new Uint8Array(buffer), function(bit) {
    return ('00' + bit.toString(16)).slice(-2);
  });
  return hexArr.join('');
}

module.hex2a = (hexx) => {
  var hex = hexx.toString(); //force conversion
  var str = '';
  for (var i = 0; i < hex.length && hex.substr(i, 2) !== '00'; i += 2) str += String.fromCharCode(parseInt(hex.substr(
    i, 2), 16));
  return str;
}

// 16进制转ArrayBuffer
module.hex2ab = (hex) => {
  var typedArray = new Uint8Array(hex.match(/[\da-f]{2}/gi).map(function(h) {
    return parseInt(h, 16)
  }))
  return typedArray.buffer
}

// 十六进制转字符串
module.hexToStr = (hexx) => {
  let hex = hexx.toString()
  let str = "",
    len = hex.length / 2;
  for (var i = 0; i < len; i++) {
    if (hex.substr(i * 2, 2) !== '00') {
      str += String.fromCharCode(parseInt(hex.substr(i * 2, 2), 16))
    }
  }
  return str
}

// 字符串转16进制
module.strToHex = (strValue) => {
  let strVal = strValue.toString()
  let str = ''
  for (let i = 0; i < strVal.length; i++) {
    str += strVal.charCodeAt(i).toString(16)
  }
  return str.toLocaleUpperCase()
}

// 平整度，垂直度，极差
const units = [{
    value: '01',
    sign: '+',
    label: 'mm'
  },
  {
    value: '02',
    sign: '+',
    label: 'mm'
  },
  {
    value: '11',
    sign: '-',
    label: 'mm'
  },
  {
    value: '12',
    sign: '-',
    label: 'mm'
  }
]

module.hexToDecimalism = (hexx) => {
  let hexStr = hexx.toString()
  console.log('hex', hexStr);
  let hex = hexStr.match(/be(\S*)ed/)[1]
  let arr = []
  for (let i = 0; i < hex.length; i += 2) {
    arr.push(hex.substr(i, 2))
  }
  // 包类型
  let dataStr = ''
  switch (arr[0]) {
    // 垂直
    case '02':
      let unit = units.find(item => item.value === arr[1])
      let data = (parseInt(arr[2], 16) * (2 ** 8) + parseInt(arr[3], 16)) / 100
      // dataStr = `${unit.sign}${data}${unit.label}`
      dataStr = `${data}${unit.label}`
      break
      // 极差
    case '05':
      dataStr = `${parseInt(`${arr[arr.length-2]}${arr[arr.length-1]}`, 16)}mm`
      break
      // 平整
    case '03':
      dataStr = `${parseInt(arr[2],16)}mm`
      break
      // 后续可加
    case '04':
      dataStr = ''
      break
    default:
      console.log('包类型未定义');
      return
  }
  return dataStr
}

// 蓝牙连接列表 (弃用)
// const bluetoothList = [{
//     name: '智能测距仪设备',
//     deviceId: 'B0:B1:13:75:91:AA', // 设备ID
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能测距仪设备',
//     deviceId: '30:E2:83:9D:86:79',
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB',
//   },
//   {
//     name: '智能测距仪设备',
//     deviceId: '30:E2:83:9D:7A:68',
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB',
//   },
//   {
//     name: '智能回弹仪设备', // 南秀
//     deviceId: '00:0C:BF:0C:83:49', // 设备ID
//     serviceId: '49535343-FE7D-4AE5-8FA9-9FAFD205E455',
//     characteristicId: '49535343-1E4D-4BD9-BA61-23C647249616', // 可通信
//     writrCharacteristicId: '49535343-8841-43F4-A8D4-ECBE34729BB3' ,// 可发送指令
//     startSampling: '24535253F8230D0A', // 开始采样指令
//     endSampling: '24455253EA230D0A' // 结束采样指令
//   },
//   {
//     0000FFE0-0000-1000-8000-00805F9B34FB
//     name: '智能高强回弹仪设备', // 中回
//     deviceId: '00:0C:BF:12:1F:46', // 设备ID
//     serviceId: '49535343-FE7D-4AE5-8FA9-9FAFD205E455',
//     characteristicId: '49535343-1E4D-4BD9-BA61-23C647249616', // 可通信
//     writrCharacteristicId: '49535343-8841-43F4-A8D4-ECBE34729BB3' ,// 可发送指令
//     startSampling: '24535253F8230D0A',
//     endSampling: '24455253EA230D0A'
//   },
//   {
//     name: '智能靠尺设备-平整度垂直度',
//     deviceId: '9C:A5:25:BD:08:77', // 设备ID
//     serviceId: '0003CDD0-0000-1000-8000-00805F9B0131',
//     characteristicId: '0003CDD1-0000-1000-8000-00805F9B0131'
//   },
//   {
//     name: '智能靠尺设备-平整度垂直度',
//     deviceId: 'D4:AD:20:57:90:9F', // 设备ID
//     serviceId: '0003CDD0-0000-1000-8000-00805F9B0131',
//     characteristicId: '0003CDD1-0000-1000-8000-00805F9B0131'
//   },
//   {
//     name: '智能靠尺设备-平整度垂直度',
//     deviceId: '9C:A5:25:BD:08:8B', // 设备ID
//     serviceId: '0003CDD0-0000-1000-8000-00805F9B0131',
//     characteristicId: '0003CDD1-0000-1000-8000-00805F9B0131'
//   },
//   {
//     name: '智能靠尺设备-极差',
//     deviceId: '48:87:2D:64:FD:8A', // 设备ID
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能靠尺设备-极差',
//     deviceId: '48:87:2D:66:F9:1A', // 设备ID
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能靠尺设备-极差',
//     deviceId: '48:87:2D:66:F8:EA', // 设备ID
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能卷尺设备',
//     deviceId: '35:53:0A:04:00:0A', // 设备ID
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能卷尺设备',
//     deviceId: 'A5:5A:09:05:8B:25',
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能卷尺设备',
//     deviceId: 'A5:5A:09:05:8F:42',
//     serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
//   },
//   {
//     name: '智能回弹仪设备', // 中回
//     deviceId: 'F2:01:46:FF:FF:FF', // 设备ID
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
//     writrCharacteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
//     startSampling: '24535253F8230D0A',
//     endSampling: '24455253EA230D0A'
//   },
//   {
//     name: '智能高强回弹仪设备', // 中回
//     deviceId: 'FF:01:1A:FF:FF:FF', // 设备ID
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
//     writrCharacteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
//     startSampling: '24535253F8230D0A',
//     endSampling: '24455253EA230D0A'
//   },
//   {
//     name: '智能阴阳角尺设备',
//     deviceId: '84:C6:92:F4:D1:FA',
//     serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
//     characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
//   },
// ]

// 导出蓝牙列表以及对应方法 (弃用)
// module.bluetoothList = bluetoothList
// module.bluetoothListOflink = (deviceId) => {
//   return bluetoothList.find(item => deviceId === item.deviceId)
// }

// 蓝牙连接列表 (启用)
const bluetoothList = [{
    name: '智能测距仪设备',
    type: 'S2',
    serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
  },
  {
    name: '智能卷尺设备',
    type: 'DT20',
    serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
  },
  {
    name: '智能阴阳角尺设备',
    type: '智能角尺',
    serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
  },
  {
    name: '智能靠尺设备-平整度垂直度',
    type: 'NanXiu',
    serviceId: '0003CDD0-0000-1000-8000-00805F9B0131',
    characteristicId: '0003CDD1-0000-1000-8000-00805F9B0131'
  },
  {
    name: '智能靠尺设备-极差',
    type: 'NanXiu-JGBT',
    serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
  },
  {
    name: '智能回弹仪设备', // 中回
    type: 'ZC3-U',
    serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    writrCharacteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    startSampling: '24535253F8230D0A',
    endSampling: '24455253EA230D0A'
  },
  {
    name: '智能高强回弹仪设备', // 中回
    type: 'ZC450-U',
    serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    writrCharacteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    startSampling: '24535253F8230D0A',
    endSampling: '24455253EA230D0A'
  },
  {
    name: '智能回弹仪设备', // 南秀(旧)
    type: 'ZC225-B',
    serviceId: '49535343-FE7D-4AE5-8FA9-9FAFD205E455',
    characteristicId: '49535343-1E4D-4BD9-BA61-23C647249616',
    writrCharacteristicId: '49535343-8841-43F4-A8D4-ECBE34729BB3',
    startSampling: '24535253F8230D0A',
    endSampling: '24455253EA230D0A'
  },
  {
    name: '智能高强回弹仪设备', // 中回-南秀(旧)
    type: 'HTY-ZC450-E',
    serviceId: '49535343-FE7D-4AE5-8FA9-9FAFD205E455',
    characteristicId: '49535343-1E4D-4BD9-BA61-23C647249616',
    writrCharacteristicId: '49535343-8841-43F4-A8D4-ECBE34729BB3',
    startSampling: '24535253F8230D0A',
    endSampling: '24455253EA230D0A'
  },
  {
    name: '智能钢筋扫描仪设备',
    type: 'GY71',
    serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
    characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    writrCharacteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
    startSampling: '4843410000000D410000575231',
    endSampling: '4843410000000D410000575200',
  },
  {
    name: '智能楼板测厚仪设备',
    type: 'HD91',
    serviceId: 'B810093A-9130-B955-2BA1-29A9807C0F69',
    characteristicId: '00008001-0000-1000-8000-00805F9B34FB',
    writrCharacteristicId: '00008002-0000-1000-8000-00805F9B34FB',
    startSampling: '4843410000000D410000575231',
    endSampling: '4843410000000D410000575200'
  },
  // 后续朗睿科技
  {
	name: '智能测距仪设备',
	type: 'SNDWAY',
	serviceId: '0000FFB0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFB2-0000-1000-8000-00805F9B34FB'
  },
  {
	name: '智能塞尺设备',
	type: 'P469190023',
	serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
  },
  {
	name: '智能极差仪设备',
	type: 'LS723H-20E4B4',
	serviceId: '00001000-0000-1000-8000-00805F9B34FB',
	characteristicId: '00001002-0000-1000-8000-00805F9B34FB'
  },
  {
	name: '智能阴阳角尺设备',
	type: 'P522110005',
	serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'  
  },
  {
	name: '智能靠尺设备',
	type: 'P323190017',
	serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB'
  },
  {
	name: '智能回弹仪设备',
	type: 'HC69210085',
	serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFE1-0000-1000-8000-00805F9B34FB',
	writrCharacteristicId: '0000FFE2-0000-1000-8000-00805F9B34FB',
	startSampling: '22110000',
	endSampling: '22220000'
  },
  {
	name: '智能高强回弹仪设备',
	type: 'HK69200076',
	serviceId: '0000FFE0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FF01-0000-1000-8000-00805F9B34FB',
	writrCharacteristicId: '0000FF02-0000-1000-8000-00805F9B34FB',
	startSampling: '22110000',
	endSampling: '22220000'
  },
  {
	name: '智能钢筋扫描仪设备',
	type: 'G169180111',
	serviceId: '0000FFF0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFF1-0000-1000-8000-00805F9B34FB',
	writrCharacteristicId: '0000FFF2-0000-1000-8000-00805F9B34FB',
	startSampling: '',
	endSampling: 'FFFD02'
  },
  {
	name: '智能楼板测厚仪设备',
	type: 'B369180026',
	serviceId: '0000FFF0-0000-1000-8000-00805F9B34FB',
	characteristicId: '0000FFF1-0000-1000-8000-00805F9B34FB'
  }
]

// 导出蓝牙列表以及对应方法 (启用)
module.bluetoothList = bluetoothList
module.bluetoothListOflink = (name = '') => {
  const arr = bluetoothList.filter(item => item.type && name.toLocaleUpperCase().includes(item.type
    .toLocaleUpperCase()))
  if (arr.length > 1) return arr.find(item => item.type.toLocaleUpperCase() === name.toLocaleUpperCase())
  return arr.find(item => item)
}

// 各项目阶段所需设备
const equipsOfcurrStage = [{
    stage: '混凝土工程-回弹强度',
    // 回弹仪/高强回弹仪
    // equips: ['00:0C:BF:0C:83:49', '00:0C:BF:12:1F:46', 'F2:01:46:FF:FF:FF', 'FF:01:1A:FF:FF:FF']
    equips: ['ZC3-U', 'ZC450-U', 'ZC225-B', 'HTY-ZC450-E', 'HC69210085', 'HK69200076']
  },
  {
    stage: '混凝土工程-截面尺寸',
    // 卷尺/激光测距仪
    // equips: ['35:53:0A:04:00:0A', 'B0:B1:13:75:91:AA', '30:E2:83:9D:86:79', '30:E2:83:9D:7A:68', 'A5:5A:09:05:8B:25', 'A5:5A:09:05:8F:42']
    equips: ['S2', 'DT20', 'SNDWAY']
  },
  {
    stage: '混凝土工程-表面平整度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P469190023']
  },
  {
    stage: '混凝土工程-垂直度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P323190017']
  },
  {
    stage: '混凝土工程-楼板厚度偏差',
    // 楼板测厚仪
    equips: ['HD91', 'B369180026']
  },
  {
    stage: '混凝土工程-钢筋保护层厚度',
    // 钢筋扫描仪
    equips: ['GY71', 'G169180111']
  },
  {
    stage: '砌筑工程-表面平整度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P469190023']
  },
  {
    stage: '砌筑工程-垂直度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P323190017']
  },
  {
    stage: '砌筑工程-外门窗洞口尺寸偏差',
    // 卷尺/激光测距仪
    // equips: ['35:53:0A:04:00:0A', 'B0:B1:13:75:91:AA', '30:E2:83:9D:86:79', '30:E2:83:9D:7A:68', 'A5:5A:09:05:8B:25', 'A5:5A:09:05:8F:42']
    equips: ['S2', 'DT20', 'SNDWAY']
  },
  {
    stage: '抹灰工程-墙面表面平整度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P469190023']
  },
  {
    stage: '抹灰工程-墙面垂直度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P323190017']
  },
  {
    stage: '抹灰工程-阴阳角方正',
    // 阴阳角检测尺
    // equips: ['84:C6:92:F4:D1:FA']
    equips: ['智能角尺', 'P522110005']
  },
  {
    stage: '抹灰工程-房间开间/进深偏差',
    // 卷尺/激光测距仪
    // equips: ['35:53:0A:04:00:0A', 'B0:B1:13:75:91:AA', '30:E2:83:9D:86:79', '30:E2:83:9D:7A:68', 'A5:5A:09:05:8B:25', 'A5:5A:09:05:8F:42']
    equips: ['S2', 'DT20', 'SNDWAY']
  },
  {
    stage: '抹灰工程-地面表面平整度',
    // 靠尺
    // equips: ['9C:A5:25:BD:08:77', 'D4:AD:20:57:90:9F', '9C:A5:25:BD:08:8B']
    equips: ['NanXiu', 'P469190023']
  },
  {
    stage: '抹灰工程-地面水平度极差',
    // 极差仪
    // equips: ['48:87:2D:64:FD:8A', '48:87:2D:66:F9:1A', '48:87:2D:66:F8:EA']
    equips: ['NanXiu-JGBT', 'LS723H-20E4B4']
  },
  {
    stage: '抹灰工程-户内门洞尺寸偏差',
    // 卷尺/激光测距仪
    // equips: ['35:53:0A:04:00:0A', 'B0:B1:13:75:91:AA', '30:E2:83:9D:86:79', '30:E2:83:9D:7A:68', 'A5:5A:09:05:8B:25', 'A5:5A:09:05:8F:42']
    equips: ['S2', 'DT20', 'SNDWAY']
  },
  {
    stage: '抹灰工程-外墙窗内侧墙体厚度极差',
    // 卷尺/激光测距仪
    // equips: ['35:53:0A:04:00:0A', 'B0:B1:13:75:91:AA', '30:E2:83:9D:86:79', '30:E2:83:9D:7A:68', 'A5:5A:09:05:8B:25', 'A5:5A:09:05:8F:42']
    equips: ['S2', 'DT20', 'SNDWAY']
  },
]

// module.equipsOfcurrStage = equipsOfcurrStage
module.isEquipsOfcurrStage = ({
  equipName = '',
  stageName = ''
} = {}) => {
  if (equipName === '' || stageName === '') return
  const currNeededEquips = equipsOfcurrStage.find(item => item.stage.includes(stageName))
  // console.log('当前项目阶段所需设备====>', currNeededEquips);
  const currEquip = module.bluetoothListOflink(equipName)
  // console.log('当前设备', currEquip);
  const isNeeded = currNeededEquips?.equips.some(item => currEquip.type && item === currEquip.type)
  // console.log('is', isNeeded);
  return isNeeded
}

// 朗睿科技数据解析
module.fmData = formatData

// 任务状态
const statusList = [{
    id: "START",
    name: "开始",
  },
  {
    id: "EXECUTE",
    name: "执行中",
  },
  {
    id: "SUBMIT_PASS",
    name: "合格率通过",
  },
  {
    id: "SUBMIT_FAIL",
    name: "合格率不通过",
  },
  {
    id: "CLOSE",
    name: "关闭",
  },
  {
    id: "ISSUE",
    name: "爆点整改申请",
  },
  {
    id: "RECTIFY_AUDIT_01",
    name: "爆点审核通过",
  },
  {
    id: "RECTIFY_ISSUE_RELEASE",
    name: "爆点整改",
  },
  {
    id: "AUDIT_01",
    name: "一级审核通过",
  },
  {
    id: "AUDIT_02",
    name: "二级审核通过",
  },
  {
    id: "RECTIFY_AUDIT_FAIL",
    name: "二次爆点整改",
  }
]
module.getTaskSt = (status) => {
  if (!status) return
  return statusList.find(item => item.id === status).name ?? ''
}

export default module