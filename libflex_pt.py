
def flexCategory(data):
    content = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": str(data['images']),
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "2:3",
                    "gravity": "top"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "size": "xl",
                                    "color": "#FFFAFA",
                                    "weight": "bold",
                                    "align": "center",
                                    "text": str(data['category'])
                                },
                                {
                                    "type": "text",
                                    "text": str(data['name']),
                                    "align": "center",
                                    "color": "#FFFAFA"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "text",
                                            "text": "ดูสินค้า",
                                            "color": "#4F4F4Fcc",
                                            "flex": 0,
                                            "offsetTop": "-2px",
                                            "margin": "none",
                                            "size": "lg"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "spacing": "sm",
                                               "cornerRadius": "1px",
                                               "backgroundColor": "#FFFAFA",
                                               "action": {
                                                   "type": "message",
                                                   "label": "action",
                                                   "text": str(data['name']),
                                    }
                                },
                                {
                                    "type": "filler"
                                }
                            ],
                            "spacing": "sm",
                                       "margin": "xxl",
                                       "height": "35px",
                                       "backgroundColor": "#FFFAFA",
                                       "cornerRadius": "2px"
                        }
                    ],
                    "position": "absolute",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#9C8E7Ecc",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "icon",
                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/s240x240/216072788_187451826767711_6891818905806366978_n.png?_nc_cat=100&ccb=1-3&_nc_sid=aee45a&_nc_eui2=AeG-qqTG6phiVkQX7W59yS2vkSXaeqT1_rSRJdp6pPX-tHQgrpXHEf33jBpm8oQBHpZTHWHEnwMTOr7Y8fgQmEo2&_nc_ohc=iGbA_ZB5ae4AX_q-JrT&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=c5bc4f6e907b7e8b9adaf362f080112e&oe=6128A8FC",
                            "size": "220px",
                            "margin": "45px",
                            "offsetTop": "-70px"
                        }
                    ],
                    "position": "absolute"
                }
            ],
            "paddingAll": "0px"
        }
    }
    return content


def flexProduct(data):
    content = {
        "type": "bubble",
        "body": {
                "type": "box",
            "layout": "vertical",
            "contents": [
                        {
                            "type": "image",
                            "url": str(data['images']),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(data['name']),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "ราคา "+str(data['price'])+ " บาท",
                                            "color": "#FFFAFA"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(data['description']),
                                            "color": "#FFFAFA"
                                        },
                                        {
                                            "type": "text",
                                            "text": "จำนวน " +str(data['stock'])+ " ชิ้น",
                                            "color": "#FFFAFA"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(data['Color']),
                                            "color": "#FFFAFA"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(data['Size']),
                                            "color": "#FFFAFA"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "สั่งซื้อสินค้า",
                                                    "color": "#4F4F4Fcc",
                                                    "flex": 0,
                                                    "offsetTop": "0px",
                                                    "size": "sm"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "action": {
                                                "type": "message",
                                                "label": "สั่งซื้อ",
                                                "text": 'สั่งซื้อ : ' + str(data['name']),
                                            },
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "cornerRadius": "2px",
                                    "spacing": "sm",
                                    "margin": "xxl",
                                    "backgroundColor": "#FFFAFA",
                                    "width": "150px",
                                    "offsetStart": "60px",
                                    "height": "27px"
                                },
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#9C8E7Ecc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/s240x240/216072788_187451826767711_6891818905806366978_n.png?_nc_cat=100&ccb=1-3&_nc_sid=aee45a&_nc_eui2=AeG-qqTG6phiVkQX7W59yS2vkSXaeqT1_rSRJdp6pPX-tHQgrpXHEf33jBpm8oQBHpZTHWHEnwMTOr7Y8fgQmEo2&_nc_ohc=iGbA_ZB5ae4AX_q-JrT&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=c5bc4f6e907b7e8b9adaf362f080112e&oe=6128A8FC",
                                    "size": "220px",
                                    "margin": "45px",
                                    "offsetTop": "-70px"
                                }
                            ],
                            "position": "absolute"
                        }
            ],
            "paddingAll": "0px"
        }
    }

    return content


def flexCart_product(data):
    content = {
        "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(data['productname']),
                        "size": "sm",
                        "color": "#555555",
                        "flex": 4
                    },
                    {
                        "type": "text",
                        "text": "x" + str(data['qty']),
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": str(f"{data['price']:,}"),
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "flex": 1
                    }
                ]
    }
    return content


def flexCart_product_whitdel(data):
    content = {
        "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(data['productname']),
                        "size": "sm",
                        "color": "#555555",
                        "flex": 4
                    },
                    {
                        "type": "text",
                        "text": "x" + str(data['qty']),
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": str(f"{data['price']:,}"),
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
                            }
                        ],
                        "alignItems": "center",
                        "justifyContent": "center",
                        "action": {
                            "type": "message",
                            "label": "action",
                            "text": "ลบสินค้า : " + str(data['productname']),
                        }
                    }
                ]
    }
    return content


def flexCart_detail(data):
    content = {
        "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": str(data['description']),
                        "size": "sm",
                        "color": "#555555",
                        "flex": 4
                    }
                ],
        "spacing": "none",
        "margin": "none",
        "offsetTop": "none",
        "paddingStart": "xl"
    }
    return content


def flexCart(data, detail):
    content = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "ตระกร้าสินค้า",
                    "weight": "bold",
                    "color": "#1DB446",
                    "size": "sm"
                },
                # {
                #     "type": "text",
                #     "text": "Umber Shop",
                #     "weight": "bold",
                #     "size": "xxl",
                #     "margin": "md"
                # },
                {
                    "type": "text",
                    "text": str(data['date']),
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": detail
                },
                {
                    "type": "separator",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xs",
                    "spacing": "xs",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "xxl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ITEMS",
                                    "size": "sm",
                                    "color": "#555555"
                                },
                                {
                                    "type": "text",
                                    "text": str(data['items']),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "total",
                                    "size": "sm",
                                    "color": "#555555"
                                },
                                {
                                    "type": "text",
                                    "text":  str(f"{data['total']:,}"),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                # {
                #     "type": "separator",
                #     "margin": "xxl"
                # },
                # {
                #     "type": "box",
                #     "layout": "horizontal",
                #     "margin": "md",
                #     "contents": [
                #         {
                #             "type": "button",
                #             "action": {
                #                 "type": "message",
                #                 "label": "ยกเลิก",
                #                 "text": "ยกเลิก"
                #             },
                #             "style": "secondary",
                #             "margin": "none",
                #             "flex": 1
                #         },
                #         {
                #             "type": "button",
                #             "action": {
                #                 "type": "message",
                #                 "label": "ชำระเงิน",
                #                 "text": "ชำระเงิน"
                #             },
                #             "style": "primary",
                #             "flex": 2
                #         }
                #     ],
                #     "spacing": "sm"
                # }
            ]
        }
    }
    return content


def flexCheckout(data, detail):
    content = {
        "type": "bubble",
        "size": "giga",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "RECEIPT",
                    "weight": "bold",
                    "color": "#1DB446",
                    "size": "sm"
                },
                # {
                #     "type": "text",
                #     "text": "Umber Shop",
                #     "weight": "bold",
                #     "size": "xxl",
                #     "margin": "md"
                # },
                {
                    "type": "text",
                    "text": str(data['date']),
                    "size": "xs",
                    "color": "#aaaaaa",
                    "wrap": True
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xxl",
                    "spacing": "sm",
                    "contents": detail
                },
                {
                    "type": "separator",
                    "margin": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "xs",
                    "spacing": "xs",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "margin": "xxl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ITEMS",
                                    "size": "sm",
                                    "color": "#555555"
                                },
                                {
                                    "type": "text",
                                    "text": str(data['items']),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "total",
                                    "size": "sm",
                                    "color": "#555555"
                                },
                                {
                                    "type": "text",
                                    "text":  str(f"{data['total']:,}"),
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "text",
                            "text": "TRANSACTION ID",
                            "size": "xs",
                            "color": "#aaaaaa",
                            "flex": 0
                        },
                        {
                            "type": "text",
                            "text": str(data['transaction']),
                            "color": "#aaaaaa",
                            "size": "xs",
                            "align": "end"
                        }
                    ]
                }
            ]
        }
    }
    return content
