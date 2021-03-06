# You may obtain a copy of the License at 
# http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License.


from flask import Flask

# Create the flask application
app = Flask("__name__")

@app.route("/")
def hello():
    return "Hello World!\n"

@app.route("/version")
def version():
    return "hellowworld 1.0.0\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

