from flask import Flask
from flask import request, render_template
from Flipkart_Scrapper import Scrapie
import time
from selenium.webdriver.common.by import By
import logging
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})


@app.route("/", methods=["GET", "POST"])
def home_page():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/result", methods=["POST"])
def result_page():
    logging.basicConfig(filename='logs.log', level=logging.INFO, filemode="w")
    try:
        if request.method == "POST":
            search = request.form["search"]
            if bool(search) == 0:
                return render_template("index.html")
            if "/" in search:
                search_string = request.form["search"].split("/")[0]
                count = int(int(request.form["search"].split("/")[1]) / 10)
                logging.info(f"search string --{search_string}")
                logging.info(f"count---{count}")
                if bool(count) == 0:
                    count = 30
                    logging.info(f"count----{count}")
            else:
                search_string = search
                count = 30
                logging.info(f"search string --{search_string}")
                logging.info(f"count---{count}")

            scrapie_object = Scrapie()
            scrapie_object.open_page("https://www.Flipkart.com")
            logging.info("opening flipkart website")

            # for closing login page --start--
            x = scrapie_object.wait_for_element_to_be_located_by_xpath('//*[@class="_2KpZ6l _2doB4z"]')
            scrapie_object.click_element(x)
            logging.info("closing login page")
            # -- end --

            # --- search box ---
            search_box = scrapie_object.wait_for_element_to_be_located_by_class_name("_3704LK")
            scrapie_object.click_element(search_box)
            logging.info("selecting search box")
            # -- end --

            # searching in search box
            scrapie_object.type_something_in_given_element(search_box, search_string)
            ok = scrapie_object.wait_for_element_to_be_located_by_class_name("L0Z3Pu")
            scrapie_object.click_element(ok)
            logging.info("searching..")
            # --ends--

            all_items = scrapie_object.find_all_elements_of_given_class("_4rR01T")
            parent_window = scrapie_object.driver.current_window_handle
            product_name = all_items[0].text
            scrapie_object.click_element(all_items[0])
            logging.info("clicking on 1st product link")
            scrapie_object.wait_for_new_window_to_open(parent_window)
            handles = scrapie_object.driver.window_handles
            for handle in handles:
                if handle != parent_window:
                    scrapie_object.driver.switch_to.window(handle)
            logging.info("switching to new window")
            all_reviews_page = scrapie_object.wait_for_element_to_be_located_by_xpath("//*[@class='_3UAT2v _16PBlm']")
            scrapie_object.click_element(all_reviews_page)
            logging.info("opening all reviews page")
            user_names = []
            ratings = []
            headings = []
            all_comments = []
            for x in range(count):
                time.sleep(1)
                comment_box = scrapie_object.find_all_elements_by_xpath("//*[@class='col _2wzgFH K0kLPL']")

                for comments in comment_box:
                    title = comments.find_element(By.XPATH, "./div[1]").text
                    comment = comments.find_element(By.XPATH, "./div[2]").text
                    user = comments.find_element(By.XPATH, "./div[3]").text
                    rating = title.split("\n")[0]
                    heading = title.split("\n")[1]
                    if bool(user) == 0:
                        user = comments.find_element(By.XPATH, "./div[4]").text
                    user_name = user.split("\n")[0]
                    print(f"----{user_name}----{rating} :{heading}---- {comment}")
                    user_names.append(user_name)
                    ratings.append(rating)
                    headings.append(heading)
                    all_comments.append(comment)
                try:
                    next_page = scrapie_object.wait_for_element_to_be_located_by_link_text("NEXT")
                    scrapie_object.double_click(next_page)
                    scrapie_object.double_click(next_page)
                    time.sleep(1)
                except:
                    scrapie_object.close_all_windows()
                    if len(ratings) == len(all_comments) == len(headings) == len(user_names):
                        return render_template("result.html", length=len(all_comments), product_name=product_name,
                                               user_names=user_names, headings=headings, ratings=ratings,
                                               all_comments=all_comments)
                    else:
                        print("unable to pass if")

            scrapie_object.close_all_windows()
            if len(ratings) == len(all_comments) == len(headings) == len(user_names):
                return render_template("result.html", length=len(all_comments), product_name=product_name,
                                       user_names=user_names, headings=headings, ratings=ratings,
                                       all_comments=all_comments)
            else:
                print("unable to pass if")
                return "<h1>Unable to pass last if block </h1>"
    except:
        return "<h1>Something went wrong</h1>"


if __name__ == "__main__":
    app.run(debug=True)
